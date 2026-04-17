def get_top_species(df, column_name='libelle_francais', n=10):
    """
    Calcule le top N des espèces les plus représentées.
    Nettoie les valeurs manquantes pour éviter d'avoir un top "Inconnu".
    """
    # On filtre les valeurs manquantes pour avoir un vrai top
    df_clean = df.dropna(subset=[column_name])
    
    # Comptage
    top_df = df_clean[column_name].value_counts().head(n).reset_index()
    top_df.columns = ['Espece', 'Nombre']
    
    # Calcul du pourcentage pour la culture générale
    total_arbres = len(df_clean)
    top_df['Pourcentage'] = (top_df['Nombre'] / total_arbres * 100).round(2)
    
    return top_df