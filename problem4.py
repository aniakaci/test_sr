# ### Problem 4
#
# Design a queuing system. The queue should implement add, view and delete. A
# viewed message will be invisible to other workers for five seconds unless it is
# deleted. Messages should be returned in order they were added unless they have
# been deleted.
#
# The add method takes a string as a message and returns a unique id for that
# message.  The view method takes no parameters and returns a hash containing the
# next message and the unique message id assigned in the add method.  The delete
# method takes the unique message id and returns true if the message was removed
# within 5 seconds or false if we were too slow.
#
# Extra points: Do you see any problems with running this kind of queue in a
# production environment?