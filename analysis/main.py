from enum import Enum
from typing import List, Literal, TypedDict, Union

# WARNING
# This data is accurate as of Thursday, 11 March 2021, 11:43 (CET)

class ThreadKind(Enum):
  Issue = 0
  PullRequest = 1

class Thread(TypedDict):
  kind: ThreadKind
  id: int
  is_scheduled: bool
  is_assigned: bool

class ActionKind(Enum):
  Message = 0
  Review = 1
  Scheduling = 2
  ChangesPushed = 3
  Close = 4
  Discussion = 5

class ChangesPushedAction(TypedDict):
  kind: Literal[ActionKind.ChangesPushed]
  id: str

class CloseAction(TypedDict):
  kind: Literal[ActionKind.Close]

class DiscussionAction(TypedDict):
  kind: Literal[ActionKind.Discussion]
  id: int

class MessageAction(TypedDict):
  kind: Literal[ActionKind.Message]
  id: int

class ReviewAction(TypedDict):
  kind: Literal[ActionKind.Review]
  id: int

class SchedulingAction(TypedDict):
  kind: Literal[ActionKind.Scheduling]

Action = Union[CloseAction, ChangesPushedAction, DiscussionAction, MessageAction, ReviewAction, SchedulingAction]

class ResponseKind(Enum):
  Immediate = 0
  Later = 1

class Response(TypedDict):
  kind: ResponseKind
  action: Action
  thread: Thread
  # no. of days between the previous action and this response
  days: int
  # whether the response was by an external contributor
  is_external: bool

# my actions per thread to calculate the reponse rate
class ParticipatingThread(TypedDict):
  thread: Thread
  # no. of my actions
  count: int
  # whether my final action was responded to
  is_addressed: bool

issue_41991 = {
  'kind': ThreadKind.Issue,
  'id': 41991,
  'is_scheduled': False,
  'is_assigned': False,
}
pull_request_42031 = {
  'kind': ThreadKind.PullRequest,
  'id': 42031,
  'is_scheduled': False,
  'is_assigned': False,
}

issue_41317 = {
  'kind': ThreadKind.Issue,
  'id': 41317,
  'is_scheduled': True,
  'is_assigned': True,
}
pull_request_41928 = {
  'kind': ThreadKind.PullRequest,
  'id': 41928,
  'is_scheduled': True,
  'is_assigned': True,
}

pull_request_42530 = {
  'kind': ThreadKind.PullRequest,
  'id': 42530,
  'is_scheduled': False,
  'is_assigned': False,
}

issue_41775 = {
  'kind': ThreadKind.Issue,
  'id': 41775,
  'is_scheduled': False,
  'is_assigned': False,
}
pull_request_969 = {
  'kind': ThreadKind.PullRequest,
  'id': 969,
  'is_scheduled': False,
  'is_assigned': False,
}

pull_request_42952 = {
  'kind': ThreadKind.PullRequest,
  'id': 42952,
  'is_scheduled': False,
  'is_assigned': False,
}
pull_request_42952_a = {
  'kind': ThreadKind.PullRequest,
  'id': 42952,
  'is_scheduled': False,
  'is_assigned': True,
}

pull_request_42382 = {
  'kind': ThreadKind.PullRequest,
  'id': 42382,
  'is_scheduled': False,
  'is_assigned': False,
}

pull_request_42602 = {
  'kind': ThreadKind.PullRequest,
  'id': 42602,
  'is_scheduled': False,
  'is_assigned': False,
}

pull_request_42835 = {
  'kind': ThreadKind.PullRequest,
  'id': 42835,
  'is_scheduled': False,
  'is_assigned': False,
}
pull_request_42835_a = {
  'kind': ThreadKind.PullRequest,
  'id': 42835,
  'is_scheduled': False,
  'is_assigned': True,
}

issue_43096 = {
  'kind': ThreadKind.Issue,
  'id': 43096,
  'is_scheduled': False,
  'is_assigned': False,
}
pull_request_43097 = {
  'kind': ThreadKind.PullRequest,
  'id': 43097,
  'is_scheduled': False,
  'is_assigned': False,
}

issue_41956 = {
  'kind': ThreadKind.Issue,
  'id': 41956,
  'is_scheduled': False,
  'is_assigned': False,
}
issue_42548 = {
  'kind': ThreadKind.Issue,
  'id': 42548,
  'is_scheduled': False,
  'is_assigned': False,
}
issue_42318 = {
  'kind': ThreadKind.Issue,
  'id': 42318,
  'is_scheduled': False,
  'is_assigned': False,
}

responses: List[Response] = [{
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 746868593,
  },
  'thread': issue_41991,
  'days': 0,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 753854017,
  },
  'thread': issue_41991,
  'days': 14,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.ChangesPushed,
    'id': '19c68ca',
  },
  'thread': pull_request_42031,
  'days': 1,
  'is_external': False,
}, {
  'kind': ResponseKind.Later,
  'action': {
    'kind': ActionKind.Review,
    'id': 556932867,
  },
  'thread': pull_request_42031,
  'days': 3,
  'is_external': False,
}, {
  'kind': ResponseKind.Later,
  'action': {
    'kind': ActionKind.Scheduling,
  },
  'thread': pull_request_42031,
  'days': 8,
  'is_external': False,
}, {
  'kind': ResponseKind.Later,
  'action': {
    'kind': ActionKind.Close,
  },
  'thread': pull_request_42031,
  'days': 5,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 763820430,
  },
  'thread': issue_41317,
  'days': 0,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 743105025,
  },
  'thread': pull_request_41928,
  'days': 0,
  'is_external': False,
}, {
  'kind': ResponseKind.Later,
  'action': {
    'kind': ActionKind.Message,
    'id': 743356094,
  },
  'thread': pull_request_41928,
  'days': 0,
  'is_external': False,
}, {
  'kind': ResponseKind.Later,
  'action': {
    'kind': ActionKind.Message,
    'id': 743358680,
  },
  'thread': pull_request_41928,
  'days': 0,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Review,
    'id': 551865735,
  },
  'thread': pull_request_41928,
  'days': 2,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Discussion,
    'id': 546000932,
  },
  'thread': pull_request_41928,
  'days': 2,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 747095634,
  },
  'thread': pull_request_41928,
  'days': 1,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 749195594,
  },
  'thread': pull_request_41928,
  'days': 0,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 749685748,
  },
  'thread': pull_request_41928,
  'days': 0,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 751852447,
  },
  'thread': pull_request_41928,
  'days': 0,
  'is_external': False,
}, {
  'kind': ResponseKind.Later,
  'action': {
    'kind': ActionKind.Scheduling,
  },
  'thread': pull_request_41928,
  'days': 2,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 758120780,
  },
  'thread': pull_request_41928,
  'days': 0,
  'is_external': False,
}, {
  'kind': ResponseKind.Later,
  'action': {
    'kind': ActionKind.Review,
    'id': 565672512,
  },
  'thread': pull_request_41928,
  'days': 12,
  'is_external': False,
}, {
  'kind': ResponseKind.Later,
  'action': {
    'kind': ActionKind.Message,
    'id': 758293970,
  },
  'thread': pull_request_41928,
  'days': 1,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Review,
    'id': 578642953,
  },
  'thread': pull_request_42530,
  'days': 0,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 769687104,
  },
  'thread': pull_request_42530,
  'days': 0,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 772135827,
  },
  'thread': pull_request_42530,
  'days': 2,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 754768730,
  },
  'thread': pull_request_969,
  'days': 1,
  'is_external': True,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 784344870,
  },
  'thread': pull_request_969,
  'days': 49,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Scheduling,
  },
  'thread': pull_request_42952,
  'days': 7,
  'is_external': False,
}, {
  'kind': ResponseKind.Later,
  'action': {
    'kind': ActionKind.Close,
  },
  'thread': pull_request_42952_a,
  'days': 1,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Scheduling,
  },
  'thread': pull_request_42382,
  'days': 8,
  'is_external': False,
}, {
  'kind': ResponseKind.Later,
  'action': {
    'kind': ActionKind.Review,
    'id': 784344870,
  },
  'thread': pull_request_42382,
  'days': 3,
  'is_external': True,
}, {
  'kind': ResponseKind.Later,
  'action': {
    'kind': ActionKind.Review,
    'id': 579554118,
  },
  'thread': pull_request_42382,
  'days': 0,
  'is_external': True,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Scheduling,
  },
  'thread': pull_request_42382,
  'days': 23,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Scheduling,
  },
  'thread': pull_request_42602,
  'days': 8,
  'is_external': False,
}, {
  'kind': ResponseKind.Later,
  'action': {
    'kind': ActionKind.Scheduling,
  },
  'thread': pull_request_42602,
  'days': 21,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 788963071,
  },
  'thread': pull_request_42835,
  'days': 13,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Review,
    'id': 608233848,
  },
  'thread': pull_request_42835_a,
  'days': 5,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Scheduling,
  },
  'thread': issue_43096,
  'days': 3,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 744720538,
  },
  'thread': issue_41956,
  'days': 0,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 769940334,
  },
  'thread': issue_42548,
  'days': 0,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 759745196,
  },
  'thread': issue_42318,
  'days': 0,
  'is_external': False,
}, {
  'kind': ResponseKind.Immediate,
  'action': {
    'kind': ActionKind.Message,
    'id': 760395837,
  },
  'thread': issue_42318,
  'days': 0,
  'is_external': False,
}]

threads: List[ParticipatingThread] = [{
  'thread': issue_41991,
  'count': 2,
  'is_addressed': True,
}, {
  'thread': pull_request_42031,
  'count': 1,
  'is_addressed': True,
}, {
  'thread': issue_41317,
  'count': 1,
  'is_addressed': True,
}, {
  'thread': pull_request_41928,
  'count': 7,
  'is_addressed': True,
}, {
  'thread': pull_request_42530,
  'count': 3,
  'is_addressed': True,
}, {
  'thread': issue_41775,
  'count': 1,
  'is_addressed': False,
}, {
  'thread': pull_request_969,
  'count': 3,
  'is_addressed': False,
}, {
  'thread': pull_request_42952,
  'count': 1,
  'is_addressed': True,
}, {
  'thread': pull_request_42382,
  'count': 4,
  'is_addressed': False,
}, {
  'thread': pull_request_42602,
  'count': 1,
  'is_addressed': False,
}, {
  'thread': pull_request_42835,
  'count': 2,
  'is_addressed': True,
}, {
  'thread': issue_43096,
  'count': 1,
  'is_addressed': False,
}, {
  'thread': pull_request_43097,
  'count': 1,
  'is_addressed': False,
}, {
  'thread': issue_41956,
  'count': 1,
  'is_addressed': True,
}, {
  'thread': issue_42548,
  'count': 1,
  'is_addressed': True,
}, {
  'thread': issue_42318,
  'count': 2,
  'is_addressed': True,
}]

def response_rate(threads: List[ParticipatingThread]) -> float:
  actions = sum([thread['count'] for thread in threads])
  addressed_actions = sum([thread['count'] if thread['is_addressed'] else thread['count'] - 1 for thread in threads])
  return addressed_actions / actions

def absolute_response_rate(threads: List[ParticipatingThread]) -> float:
  addressed_threads = sum([1 if thread['is_addressed'] else 0 for thread in threads])
  return addressed_threads / len(threads)

print('response rate:', response_rate(threads), ';', len(threads))
print('absolute response rate:', absolute_response_rate(threads), ';', len(threads))

issue_threads = [thread for thread in threads if thread['thread']['kind'] == ThreadKind.Issue]
pull_request_threads = [thread for thread in threads if thread['thread']['kind'] == ThreadKind.PullRequest]
print('issue response rate:', response_rate(issue_threads), ';', len(issue_threads))
print('issue absolute response rate:', absolute_response_rate(issue_threads), ';', len(issue_threads))
print('pull request response rate:', response_rate(pull_request_threads), ';', len(pull_request_threads))
print('pull request absolute response rate:', absolute_response_rate(pull_request_threads), ';', len(pull_request_threads))

def response_time(responses: List[Response]) -> float:
  response_times = sum([response['days'] for response in responses])
  return response_times / len(responses)

print('response time:', response_time(responses), 'days', ';', len(responses))

immediate_responses = [response for response in responses if response['kind'] == ResponseKind.Immediate]
later_responses = [response for response in responses if response['kind'] == ResponseKind.Later]
print('immediate response time:', response_time(immediate_responses), 'days', ';', len(immediate_responses))
print('later response time:', response_time(later_responses), 'days', ';', len(later_responses))

issue_responses = [response for response in responses if response['thread']['kind'] == ThreadKind.Issue]
pull_request_responses = [response for response in responses if response['thread']['kind'] == ThreadKind.PullRequest]
print('issue response time:', response_time(issue_responses), 'days', ';', len(issue_responses))
print('pull request response time:', response_time(pull_request_responses), 'days', ';', len(pull_request_responses))

pull_request_internal_responses = [response for response in responses if response['thread']['kind'] == ThreadKind.PullRequest and not response['is_external']]
print('pull request response time (not external):', response_time(pull_request_internal_responses), 'days', ';', len(pull_request_internal_responses))

unassigned_responses = [response for response in responses if not response['thread']['is_assigned']]
assigned_responses = [response for response in responses if response['thread']['is_assigned']]
print('unassigned response time:', response_time(unassigned_responses), 'days', ';', len(unassigned_responses))
issue_responses = [response for response in unassigned_responses if response['thread']['kind'] == ThreadKind.Issue]
pull_request_responses = [response for response in unassigned_responses if response['thread']['kind'] == ThreadKind.PullRequest]
print('unassigned issue response time:', response_time(issue_responses), 'days', ';', len(issue_responses))
print('unassigned pull request response time:', response_time(pull_request_responses), 'days', ';', len(pull_request_responses))
immediate_responses = [response for response in unassigned_responses if response['kind'] == ResponseKind.Immediate]
later_responses = [response for response in unassigned_responses if response['kind'] == ResponseKind.Later]
print('unassigned immediate response time:', response_time(immediate_responses), 'days', ';', len(immediate_responses))
print('unassigned later response time:', response_time(later_responses), 'days', ';', len(later_responses))
print('assigned response time:', response_time(assigned_responses), 'days', ';', len(assigned_responses))
issue_responses = [response for response in assigned_responses if response['thread']['kind'] == ThreadKind.Issue]
pull_request_responses = [response for response in assigned_responses if response['thread']['kind'] == ThreadKind.PullRequest]
print('assigned issue response time:', response_time(issue_responses), 'days', ';', len(issue_responses))
print('assigned pull request response time:', response_time(pull_request_responses), 'days', ';', len(pull_request_responses))
immediate_responses = [response for response in assigned_responses if response['kind'] == ResponseKind.Immediate]
later_responses = [response for response in assigned_responses if response['kind'] == ResponseKind.Later]
print('assigned immediate response time:', response_time(immediate_responses), 'days', ';', len(immediate_responses))
print('assigned later response time:', response_time(later_responses), 'days', ';', len(later_responses))
print('assigned response time factor:', response_time(unassigned_responses) / response_time(assigned_responses))

unscheduled_responses = [response for response in responses if not response['thread']['is_scheduled']]
scheduled_responses = [response for response in responses if response['thread']['is_scheduled']]
print('unscheduled response time:', response_time(unscheduled_responses), 'days', ';', len(unscheduled_responses))
issue_responses = [response for response in unscheduled_responses if response['thread']['kind'] == ThreadKind.Issue]
pull_request_responses = [response for response in unscheduled_responses if response['thread']['kind'] == ThreadKind.PullRequest]
print('unscheduled issue response time:', response_time(issue_responses), 'days', ';', len(issue_responses))
print('unscheduled pull request response time:', response_time(pull_request_responses), 'days', ';', len(pull_request_responses))
immediate_responses = [response for response in unscheduled_responses if response['kind'] == ResponseKind.Immediate]
later_responses = [response for response in unscheduled_responses if response['kind'] == ResponseKind.Later]
print('unscheduled immediate response time:', response_time(immediate_responses), 'days', ';', len(immediate_responses))
print('unscheduled later response time:', response_time(later_responses), 'days', ';', len(later_responses))
print('scheduled response time:', response_time(scheduled_responses), 'days', ';', len(scheduled_responses))
issue_responses = [response for response in scheduled_responses if response['thread']['kind'] == ThreadKind.Issue]
pull_request_responses = [response for response in scheduled_responses if response['thread']['kind'] == ThreadKind.PullRequest]
print('scheduled issue response time:', response_time(issue_responses), 'days', ';', len(issue_responses))
print('scheduled pull request response time:', response_time(pull_request_responses), 'days', ';', len(pull_request_responses))
immediate_responses = [response for response in scheduled_responses if response['kind'] == ResponseKind.Immediate]
later_responses = [response for response in scheduled_responses if response['kind'] == ResponseKind.Later]
print('scheduled immediate response time:', response_time(immediate_responses), 'days', ';', len(immediate_responses))
print('scheduled later response time:', response_time(later_responses), 'days', ';', len(later_responses))
print('scheduled response time factor:', response_time(unscheduled_responses) / response_time(scheduled_responses))

unassigned_unscheduled_responses = [response for response in responses if not response['thread']['is_assigned'] and not response['thread']['is_scheduled']]
print('unassigned & unscheduled response time:', response_time(unassigned_unscheduled_responses), 'days', ';', len(unassigned_unscheduled_responses))
unassigned_unscheduled_pr_responses = [response for response in unassigned_unscheduled_responses if response['thread']['kind'] == ThreadKind.PullRequest]
print('unassigned & unscheduled pull request response time:', response_time(unassigned_unscheduled_pr_responses), 'days', ';', len(unassigned_unscheduled_pr_responses))
