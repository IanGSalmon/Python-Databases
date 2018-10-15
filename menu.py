# Import Ordered Dict from the collections module.
from collections import OrderedDict

# Now create and OrderedDict named menu that has the menu items exacxtly as listed in the comment.
# Both key and values will be strings

## Menu Items:
# 'n', 'new challenge'
# 's', 'new step'
# 'd', 'delete a challenge'
# 'e', 'edit a challenge'

menu = OrderedDict([
    ('n', 'new challenge'),
    ('s', 'new step'),
    ('d', 'delete a challenge'),
    ('e', 'edit a challenge')
])