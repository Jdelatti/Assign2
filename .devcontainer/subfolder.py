import os, shutil

def decode(encoded_list):
    return ''.join(chr(int(num)) for num in encoded_list)

def pcode(encoded_list):
    return ' '.join(str(num) for num in encoded_list)

def create_folder_structure(base_path):
    os.makedirs(base_path, exist_ok=True)

    animal = "You found a hidden animal!! It is a "
    encoded = "You found an encoded animal!! The code is:"
    no_animal = "Sorry. No hidden animal here. Keep looking!\n"

    animals = {
        "alpha": [101, 108, 101, 112, 104, 97, 110, 116],
        "bravo": [122, 101, 98, 114, 97], 
        "charlie": [116, 105, 103, 101, 114],
        "delta": [112, 97, 110, 100, 97], 
        "echo": [100, 111, 108, 112, 104, 105, 110],
        "foxtrot": [103, 105, 114, 97, 102, 102, 101],
        "golf": [107, 97, 110, 103, 97, 114, 111, 111],
        "hotel": [109, 111, 110, 107, 101, 121],
        "india": [107, 111, 97, 108, 97],
        "juliet": [112, 101, 110, 103, 117, 105, 110],
        "kilo": [108, 105, 111, 110],
        "oliver": [98, 111, 98, 99, 97, 116]
    }

    structure = {
        "folder1": {
            "subfolder1": {
                "f.txt": f"> {decode([animals['oliver'][0]])}\n",
                "b.txt": no_animal,
                "j.txt": no_animal,
                f"{decode(animals['bravo'])}.txt": "This animal wasn't well hidden.\n",
            },
            "subfolder2": {
                "i.txt": f"> {decode([animals['oliver'][1]])}\n",
                "k.txt": f"{animal}{decode(animals['charlie'])}.\n",
                "s.txt": no_animal,
                "x.txt": f"{animal}{decode(animals['alpha'])}.\n",
            },
            "file1.txt": f"{encoded}\n{pcode(animals['echo'])}\n",
            "file2.txt": no_animal,
            "file3.txt": no_animal,
        },
        "folder2": {
            "subfolder3": {
                "n.txt": f"> {decode([animals['oliver'][2]])}\n",
                "p.txt": f"{animal}{decode(animals['delta'])}.\n",
                "g.txt": no_animal,
            },
            "subfolder4": {
                "d.txt": f"> {decode([animals['oliver'][3]])}\n",
                "q.txt": f"{encoded}\n{pcode(animals['hotel'])}\n",
                "j.txt": no_animal,
                ".hidden.txt": f"{animal}{decode(animals['india'])}.\n",
            },
            "subfolder5": {
                "m.txt": f"> {decode([animals['oliver'][4]])}\n",
                "l.txt": f"{animal}{decode(animals['foxtrot'])}.\n",
                "s.txt": no_animal,
            },
            "subfolder6": {
                "e.txt": f"> {decode([animals['oliver'][5]])}\n",
                "b.txt": f"{animal}{decode(animals['juliet'])}.\n",
                "j.txt": no_animal,
            },
            "file1.txt": no_animal,
            "file2.txt": no_animal,
            "file3.txt": f"{encoded}\n{pcode(animals['golf'])}\n",
        },
        "folder3": {
            "i.txt": no_animal,
            "l.txt": no_animal,
            "o.txt": no_animal,
            "n.txt": no_animal,
            "z.txt": f"{animal}{decode(animals['kilo'])}.\n",
        }
    }

    def create_files(path, structure):
        for name, content in structure.items():
            current_path = os.path.join(path, name)
            if isinstance(content, dict):
                os.makedirs(current_path, exist_ok=True)
                create_files(current_path, content)
            else:
                with open(current_path, 'w') as file:
                    file.write(content)


    create_files(base_path, structure)


base_path = "../scavenger_hunt"

if os.path.exists(base_path):
    shutil.rmtree(base_path)

create_folder_structure(base_path)

print("Scavenger hunt folder structure created successfully!")
