import os
from dotenv import load_dotenv

# The os module in Python provides a way of using operating system-dependent functionality like reading or writing to the file system.
load_dotenv()


#get the process count
# print(os.cpu_count())   
# print(os.getpid())


#Common Uses of the os Module:
#Working with Directories
""" print(os.getcwd()) 
os.mkdir('new_folder')       
os.listdir('.')  """

#Working with Files
""" os.remove('file.txt')       
os.rename('old.txt', 'new.txt')   """


#environment variables
# print(os.environ['HOME'])    
# os.environ['MY_VAR'] = '123' 

""" print(os.environ['HOME'])    
print(os.getenv('MY_VAR'))   
print(os.getenv('API_KEY'))   
 """

#Running System Commands
# print(os.system('ls')) 
# print(os.system('dir')) 

#Path Handling (using os.path)
file_path = os.path.join('folder', 'file.txt')  
# print(os.path.exists(file_path))                
# print(os.path.abspath(file_path))