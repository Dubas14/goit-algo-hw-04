from pathlib import Path

def get_cats_info(path):
    cats_info = []
    
    try:
       
        script_dir = Path(__file__).parent
        pets_path = script_dir / path
        with open(pets_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  
                if line:  
                    cat_id, cat_name, cat_age = line.split(',')
                    cat_dict = {
                        "id": cat_id,
                        "name": cat_name,
                        "age": cat_age
                    }
                    cats_info.append(cat_dict)
    except FileNotFoundError:
        print(f"Файл за шляхом {pets_path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
    
    return cats_info


path = 'pets.txt'
cats_info = get_cats_info(path)
print(cats_info)