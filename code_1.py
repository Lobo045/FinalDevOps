import os

class ClientManager:
    def __init__(self, data_folder='clients_data'):
        self.data_folder = data_folder
        self.ensure_data_folder_exists()

    def ensure_data_folder_exists(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

    def create_client(self):
        client_name = input("Ingrese el nombre del cliente: ")
        client_file_path = os.path.join(self.data_folder, f'{client_name}.txt')

        if not os.path.exists(client_file_path):
            with open(client_file_path, 'w') as client_file:
                client_file.write(f"Client Name: {client_name}\nDescription: ")
            print(f"El cliente '{client_name}' ha sido creado.")

    def edit_client(self):
        client_name = input("Cual cliente desa editar: ")
        new_name = input("Ingrese el nombre nuevo del cliente (ENTER si desea dejarlo igual): ") or client_name
        new_description = input("Ingrese nueva descripcion (ENTER si desea dejarla igual): ")

        client_file_path = os.path.join(self.data_folder, f'{client_name}.txt')

        if os.path.exists(client_file_path):
            with open(client_file_path, 'r') as client_file:
                lines = client_file.readlines()

            for i in range(len(lines)):
                if lines[i].startswith("Client Name:"):
                    lines[i] = f"Client Name: {new_name}\n"
                    if new_description:
                        lines[i + 1] = f"Description: {new_description}\n"

            with open(client_file_path, 'w') as client_file:
                client_file.writelines(lines)

            # Rename the file if the name is changed
            if new_name != client_name:
                new_client_file_path = os.path.join(self.data_folder, f'{new_name}.txt')
                os.rename(client_file_path, new_client_file_path)
                print(f"El cliente '{client_name}' ha sido renombrado a '{new_name}'.")
            else:
                print(f"El cliente '{client_name}' ha sido editado.")

        else:
            print(f"El cliente '{client_name}' no existe.")

    def delete_client(self):
        client_name = input("Ingrese el nombre del cliente que desea borrar: ")
        client_file_path = os.path.join(self.data_folder, f'{client_name}.txt')

        if os.path.exists(client_file_path):
            os.remove(client_file_path)
            print(f"El cliente '{client_name}' ha sido borrado.")
        else:
            print(f"El cliente '{client_name}' no existe.")

    def list_clients(self):
        print("Lista de clientes:")
        for file_name in os.listdir(self.data_folder):
            if file_name.endswith(".txt"):
                print(file_name[:-4]) 

if __name__ == "__main__":
    manager = ClientManager()

    while True:
        print("\nOptions:")
        print("1. Crear clientes")
        print("2. Editar clientes")
        print("3. Borrar clientes")
        print("4. Lita de clientes")
        print("5. Salir")

        choice = input("Elija una opcion (1-5): ")

        if choice == '1':
            manager.create_client()
        elif choice == '2':
            manager.edit_client()
        elif choice == '3':
            manager.delete_client()
        elif choice == '4':
            manager.list_clients()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Favor de elegir una opcion entre el 1 y el 5.")
