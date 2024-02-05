import os

class ClientManager:
    #Creamos el codigo para añadir clientes
    def __init__(self, data_folder='clients_data'):
        self.data_folder = data_folder
        self.ensure_data_folder_exists()

    def ensure_data_folder_exists(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

    def create_client(self, client_name):
        client_file_path = os.path.join(self.data_folder, f'{client_name}.txt')

        if not os.path.exists(client_file_path):
            with open(client_file_path, 'w') as client_file:
                client_file.write(f"Client Name: {client_name}\nDescription: ")

            print(f"El cliente '{client_name}' ha sido creado")

    #Creamos el codigo para editar clientes
    def edit_client(self, client_name, new_name=None, new_description=None):
        client_file_path = os.path.join(self.data_folder, f'{client_name}.txt')

        if os.path.exists(client_file_path):
            with open(client_file_path, 'r') as client_file:
                lines = client_file.readlines()

            for i in range(len(lines)):
                if lines[i].startswith("Client Name:"):
                    if new_name:
                        lines[i] = f"Client Name: {new_name}\n"
                    if new_description:
                        lines[i + 1] = f"Description: {new_description}\n"

            with open(client_file_path, 'w') as client_file:
                client_file.writelines(lines)

            # Rename the file if the name is changed
            if new_name and new_name != client_name:
                new_client_file_path = os.path.join(self.data_folder, f'{new_name}.txt')
                os.rename(client_file_path, new_client_file_path)

    #Codigo para borrar clientes
    def delete_client(self, client_name):
        client_file_path = os.path.join(self.data_folder, f'{client_name}.txt')

        if os.path.exists(client_file_path):
            os.remove(client_file_path)
            print(f"El cliente '{client_name}' ha sido borrado.")
        else:
            print(f"El cliente '{client_name}' no existe.")

if __name__ == "__main__":
    manager = ClientManager()

    while True:
        print("\nOptions:")
        print("1. Crear clientes")
        print("2. Editar cilentes")
        print("3. Borrar clientes")
        print("4. Lista de clientes")
        print("5. Salir")

        choice = input("Elija una obcion (1-5): ")

        if choice == '1':
            manager.create_client()
        elif choice == '2':
            manager.edit_client()
        elif choice == '3':
            manager.delete_client()
        elif choice == '4':
            manager.list_clients()
        elif choice == '5':
            print("Saliendo de la aplicacion.")
            break
        else:
            print("Favor de elejir un numero entre el 1 y el 5")