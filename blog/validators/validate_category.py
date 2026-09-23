from ..models import Category

def validate_category(name, description, category_id=None):
    errors = []
    if name == '':
        errors.append('Le nom est obligatoire')
    
    if description == '':
        errors.append('La description est obligatoire')
    
    if len(name) <= 4:
        errors.append('Le nom doit être supérieur à 4 caractères')
    
    if len(name) > 30:
        errors.append('Le nom doit être inférieur à 20 caractères')
    
    # Vérifier si le nom existe déjà
    category = Category.objects.filter(name=name)
    
    # Pour la modification, on exclut la catégorie actuelle
    if category_id is not None:
        category = category.exclude(id=category_id)
        
    if category.exists():
        errors.append('Cette catégorie existe déjà')
        
    return errors