# Modyfikowanie listy w funkcji

# Tworzymy funkcję.
# Stymulujemy wydruk poszczególnych projektów, dopóki pozostał jakikolwiek projekt na liście.
# Każdy wydrukowany model zostaje przeniesiony na listę completed_models.

from printing_functions import print_models as pm, show_completed_models as scm
    
# Rozpoczynamy od pewnych projektów, które mają być wydrukowane.
unprinted_designs = ['etui telefonu', 'robot pendant', 'dwunastościan']
completed_models = []

# Wywołanie tych funkcji:
pm(unprinted_designs,completed_models)
scm(completed_models)
