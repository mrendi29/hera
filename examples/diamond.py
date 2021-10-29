"""
This example showcases the classic diamond workflow that is used as an example by Argo documentation and
other libraries.
"""
from hera.v1.task import Task
from hera.v1.workflow import Workflow
from hera.v1.workflow_service import WorkflowService


def say(message: str):
    print(message)


# TODO: replace the domain and token with your own
ws = WorkflowService('my-argo-server.com', 'my-auth-token')
w = Workflow('diamond', ws)
a = Task('A', say, [{'message': 'This is task A!'}])
b = Task('B', say, [{'message': 'This is task B!'}])
c = Task('C', say, [{'message': 'This is task C!'}])
d = Task('D', say, [{'message': 'This is task D!'}])

a.next(b)  # a >> b
a.next(c)  # a >> c
b.next(d)  # b >> d
c.next(d)  # c >> d

w.add_tasks(a, b, c, d)
w.submit()