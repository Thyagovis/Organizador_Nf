import os
import shutil


def Create_dirfile():

    if "Dir.txt" not in os.listdir('./'):
        
        dir_file = open('./Dir.txt', 'w')
        dir_file.close()


def Define_diretory(diretory : str):

    dir_file = open('./Dir.txt', 'w')
    dir_file.write(diretory)
    dir_file.close


def Destination():
    
    dir_file = open('./Dir.txt', 'r')
    costumers_dir = dir_file.read()

    return costumers_dir


def MkCostumer_dir(costumer_data : list):
    
    costumer_name = costumer_data[0].split(':')
    costumer_id = costumer_data[1].split(':')

    costumer = f'{costumer_id[1]} - {costumer_name[1]}'

    costumers_dir = Destination()

    if 'Clientes' not in os.listdir(costumers_dir):

        os.mkdir(f'{costumers_dir}/Clientes')

    costumers_dir = f'{costumers_dir}/Clientes'

    if costumer not in os.listdir(costumers_dir):

        os.mkdir(f'{costumers_dir}/{costumer}')


    return f'{costumers_dir}/{costumer}'


def MoveFile(pdf : str, costumer : list):

    destination = MkCostumer_dir(costumer)

    shutil.move(pdf, destination)



