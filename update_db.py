import sqlite3

def update_database():
    """Ajoute la colonne image_url à la table dreams si elle n'existe pas"""
    try:
        conn = sqlite3.connect('dreams.db')
        c = conn.cursor()
        
        # Vérifier si la colonne existe déjà
        c.execute("PRAGMA table_info(dreams)")
        columns = [column[1] for column in c.fetchall()]
        
        if 'image_url' not in columns:
            # Ajouter la colonne image_url
            c.execute("ALTER TABLE dreams ADD COLUMN image_url TEXT")
            conn.commit()
            print("✅ Base de données mise à jour avec succès !")
        else:
            print("ℹ️ La base de données est déjà à jour.")
            
        conn.close()
        
    except Exception as e:
        print(f"❌ Erreur lors de la mise à jour de la base de données : {e}")

if __name__ == "__main__":
    print("Mise à jour de la structure de la base de données...")
    update_database()
