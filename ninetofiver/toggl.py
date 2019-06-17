"""Toggl integration."""
import logging
import datetime
from ninetofiver import models, settings
import requests
import json



logger = logging.getLogger(__name__)


def get_connector():
    """Get a toggl connector."""
    username = settings.TOGGL_API_KEY
    password = settings.TOGGL_PASSWORD
    user_agent = settings.TOGGL_USER_AGENT
    workspace_id = settings.TOGGL_WORKSPACE_ID
    url = settings.TOGGL_URL
    reporting_url = settings.TOGGL_REPORTING_URL

    return {
      "username": username,
      "password": password,
      "user_agent": user_agent,
      "workspace_id": workspace_id,
      "url": url,
      "reporting_url": reporting_url,
      "user_agent": user_agent,
    }


def get_project_choices():
    """Get toggl project choices."""
    choices = [[None, '-----------']]

    toggl = get_connector()
    r = requests.get(f'{toggl["url"]}/workspaces/{toggl["workspace_id"]}/projects',
      auth=(toggl['username'], 'api_token'),
      params={'workspace_id': toggl['workspace_id'], 'user_agent': toggl['user_agent']})

    return r


def get_user_performances(user, from_date=None, to_date=None):
    """Get toggl performances."""
    data = []
    toggl = get_connector()

    request = requests.get(f'{toggl["reporting_url"]}/details?since={from_date}&until={to_date}',
      auth=(toggl['username'], 'api_token'),
      params={'workspace_id': toggl['workspace_id'], 'user_agent': toggl['user_agent']})
    response = request.json()

    time_entry_ids = [x['id'] for x in response['data']]
    toggl_performances = (models.Performance.objects
                            .filter(timesheet__user=user, redmine_id__in=time_entry_ids)
                            .values('redmine_id', 'id'))
    toggl_performances = {str(x['redmine_id']): x['id'] for x in toggl_performances}

    # The contract ID for the given time entry is found by searching for the special contract_id tag.
    # The actual ID is suffixed with a '-' symbol.
    for time_entry in response['data']:
      performance_id = toggl_performances.get(str(time_entry['id']), None)
      contract = next((x.split('-')[1] for x in time_entry['tags'] if x.split('-')[0] == 'contract_id'), None)
      contract = int(contract) if contract else contract

      if not contract:
        continue

      date = time_entry['start'][:10]
      duration = round(time_entry['dur']/(1000*60*60), 2)

      data.append({
        'id': performance_id,
        'contract': contract,
        'redmine_id': time_entry['id'],
        'duration': duration,
        'description': time_entry['description'],
        'date': date
      })

    return data
