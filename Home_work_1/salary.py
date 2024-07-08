from pathlib import Path

def total_salary(relative_path):
    try:
        file_path = Path.cwd() / relative_path
        
        with file_path.open('r', encoding='utf-8') as file:
            lines = file.readlines()
        
        total = 0
        count = 0
        
        for line in lines:
            parts = line.strip().split(',')
            for part in parts:
                try:
                    salary = float(part)
                    total += salary
                    count += 1
                except ValueError:
                    
                    continue
        
        if count == 0:
            raise ValueError("No valid salary data found.")
        
        average = total / count
        return total, average
    
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


relative_path = "salary_file.txt"  
result = total_salary(relative_path)
if result:
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")