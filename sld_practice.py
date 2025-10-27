from knowledge_base_pasaporte import knowledge_base

def is_variable(term):
    # Se verifica si existe un término que sea una variable.
    # (es decir, las que empiezan con '?'). :p
    return isinstance(term, str) and term.startswith('?')

def unify(term1, term2, substitution=None):

    # Aquí ocurre la unificación.
    # Se comparan dos términos y devuelve la unificación si pueden ser unificados.
    
    if substitution is None:
        substitution = {}

    # ¿Términos idénticos?
    if term1 == term2:
        return substitution

    # ¿El término 1 es una variable?
    if is_variable(term1):
        if term1 in substitution:
            return unify(substitution[term1], term2, substitution)
        else:

            # En búsqueda de conflictos...
            if is_variable(term2) and term2 in substitution:
                return unify(term1, substitution[term2], substitution)
            substitution[term1] = term2
            return substitution

    # ¿El término 2 es una variable
    if is_variable(term2):
        if term2 in substitution:
            return unify(term1, substitution[term2], substitution)
        else:
            substitution[term2] = term1
            return substitution

    # ¿Son ambos tuplas? (O lo que es lo mismo: predicados con argumentos)
    if isinstance(term1, tuple) and isinstance(term2, tuple):
        if len(term1) != len(term2):
            return None

        # Unificación de cada argumento
        for arg1, arg2 in zip(term1, term2):
            substitution = unify(arg1, arg2, substitution)
            if substitution is None:
                return None
        return substitution

    return None

def apply_substitution(term, substitution):

    # Aplicando la sustitución a un término
    if not substitution:
        return term
    
    if is_variable(term):
        return substitution.get(term, term)
    
    if isinstance(term, tuple):
        return tuple(apply_substitution(arg, substitution) for arg in term)
    
    return substitution.get(term, term)

def evaluate_operation(operation, substitution):

    # Evaluando operaciones matemáticas simples
    if isinstance(operation, tuple) and len(operation) == 4:
        op, arg1, arg2, result_var = operation
        arg1_val = apply_substitution(arg1, substitution)
        arg2_val = apply_substitution(arg2, substitution)
        
        if op == 'divide' and isinstance(arg1_val, (int, float)) and isinstance(arg2_val, (int, float)):
            result = arg1_val / arg2_val
            new_substitution = substitution.copy()
            new_substitution[result_var] = result
            return new_substitution
    
    return None

def resolve_sld(goals, substitution=None, depth=0):

    # Aplicando la resolución SLD
    # Resolviendo objetivos usando la base del conocimiento
    if substitution is None:
        substitution = {}
    
    if not goals:
        return substitution
    
    current_goal = apply_substitution(goals[0], substitution)
    remaining_goals = goals[1:]
    
    print(f"{'  ' * depth}Objetivo: {current_goal}")
    
    if isinstance(current_goal, tuple) and current_goal[0] in ['divide']:
        result_sub = evaluate_operation(current_goal, substitution)
        if result_sub:
            return resolve_sld(remaining_goals, result_sub, depth + 1)
        else:
            return None
    
    if isinstance(current_goal, tuple) and current_goal[0] == 'not':
        negated_goal = current_goal[1]
        if resolve_sld([negated_goal], substitution.copy(), depth + 1) is None:
            return resolve_sld(remaining_goals, substitution, depth + 1)
        else:
            return None
    
    for clause in knowledge_base:
        head, body = clause
        new_substitution = unify(current_goal, head, substitution.copy())
        
        if new_substitution is not None:
            print(f"{'  ' * depth}✓ Unifica con: {head}")
            
            new_goals = [apply_substitution(g, new_substitution) for g in body] + remaining_goals
            
            result = resolve_sld(new_goals, new_substitution, depth + 1)
            if result is not None:
                return result
    
    print(f"{'  ' * depth}✗ No se pudo resolver: {current_goal}")
    return None

def query(goal, facts_to_add=None):

    # Algunas consultas de pacotilla que se me ocurrieron (y otras tomadas del documento)
    print(f"\n🔍 CONSULTA: {goal}")
    print("=" * 60)
    
    temp_knowledge = knowledge_base.copy()
    if facts_to_add:
        for fact in facts_to_add:
            temp_knowledge.append((fact, []))
    
    global knowledge_base_g
    original_kb = knowledge_base
    knowledge_base_g = temp_knowledge
    
    try:
        if isinstance(goal, tuple):
            goals = [goal]
        else:
            goals = [goal]
        
        result = resolve_sld(goals)
        
        print("=" * 60)
        if result:
            print(f"✅ ¡Éxito! Sustitución: {result}")
            final_result = apply_substitution(goal, result)
            print(f"📝 Respuesta: {final_result}")
            return final_result
        else:
            print("❌ No se pudo probar la consulta")
            return None
    finally:
        knowledge_base_g = original_kb

if __name__ == "__main__":
    print("---⎨ SISTEMA DE CONSULTA PARA TRÁMITE DE PASAPORTE ⎬---")
    
    print("=" * 50)
    print("\nConsulta 1: Si soy trabajador agrícola, ¿puedo sacar el pasaporte de 10 años?")
    query(('puede_vigencia', '?solicitante', '10_year'), 
          facts_to_add=[('es_trabajador_agricola', 'juan')])

    print("=" * 50)
    print("\nConsulta 2: Costo con descuento para adulto mayor")
    query(('costo_final', '?solicitante', '6_year', '?costo_final'), 
          facts_to_add=[
              ('mayor_60', 'ana'),
              ('costo', '6_year', 2350)
          ])
