def print_models(unprinted_designs,completed_models):
    """Symulujemy wydruk poszczególnych projektów, dopóki pozostał jakikolwiek projekt na liście. Każdy 
    wydrukowany model zostaje przeniesiony na listę completed_models."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Wydruk modelu: {current_design}")
        completed_models.append(current_design)
    
def show_completed_models(completed_models):
    """Wyświetla wszystkie modele, które zostały wydrukowane."""
    print("\nWydrukowane zostały następujące modele:")
    for completed_model in completed_models:
        print(completed_model)