import os, uuid, sys, pprint, pandas as pd
from azure.storage.filedatalake import DataLakeServiceClient
import time
try:  
    global service_client
        
    service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
        "https", "deepadls"), credential="LmVS8nloXT9OHIKUaniYzTCkHapSl3K3U6T5hL4wB6KX5Fky9DDFY1r63fksBJ+2xgmkIxu0ljBZlv3p+N47kQ==")
except Exception as e:
    print(e)

container = 'ny311'
directory = 'deeptesthub1'

# def master_function(container,directory):
#     try:

#         file_system_client = service_client.get_file_system_client(file_system=container)
#         directory_client = file_system_client.get_directory_client(directory)
        
#         acl_props = directory_client.get_access_control()
     
        
#         df = (acl_props['acl'])
      
#         ch = 'y'
 
#         df1 = pd.DataFrame([x for x in df.split('\n')[0].split(',')])
#         df2 = df1[0].str.split(':',expand =True)
#         user_name = input("Enter the User Object ID")
#         print(df2[1])
#         flag =0
#         for x in range(0,len(df2)):
#             if df2[1][x] == user_name :
#                  flag =1
                 
#             if flag == 1 :
#                  ans1 =input("User Already Exists\n Do you want to \n1. Change User Permission \n2. Remove User\n")
#                  if(ans1 == '1'):
#                      manage_directory_permissions(file_system_client,directory_client,user_name)
#                  elif(ans1 == '2'):
#                      remove_user(df2,user_name)
#                  else :
#                      print("Wrong Option \n Loop ends in 3..2..1 ")
#                      time.sleep(3)
#                      break 

#             else :
#                  ans2 = input("User doesnt exist \n Do you want to add this user(y/n)? ")
#                  if(ans2 == 'y' or ans2 =='Y'):
#                      add_user(df2,user_name)
#                  else: break



#         print("Current User-permissions:")
#         print(df2)
    
#     except Exception as e:
#         print(e)


def manage_directory_permissions(file_system_name, directory_name):
    try:
        
        file_system_client = service_client.get_file_system_client(file_system=file_system_name)
        directory_client = file_system_client.get_directory_client(directory_name)
        
        acl_props = directory_client.get_access_control()
     
        
        df = (acl_props['acl'])
        # var = user_name
        ch = 'y'
 
        df1 = pd.DataFrame([x for x in df.split('\n')[0].split(',')])
        df2 = df1[0].str.split(':',expand =True)
        print("Current User-permissions:")
        print(df2)
        while (ch=='y' or ch=='Y'):
            var = input("enter the username: ")
            perm  = input("enter its permission: ")
            for x in range(0,len(df2)):
                if df2[1][x] == var :
                    df2[2][x] = perm 
            ch = input("Do you want to change permission for another user (Y/N) ")
       
        print("Updated User-permissions:")
        print(df2)
        acl = ''
        x=0
        for x in range(0,len(df2)):
            for y in range(0,3):
                acl = acl + df2[y][x]
                if y<2 :
                    acl = acl +':' 
                else : 
                    acl = acl + ',' 
        
        acl_new = acl[:-1]
                
        directory_client.set_access_control(acl=acl_new)
        acl_prop = directory_client.get_access_control()
     
    except Exception as e:
        print(e)


# master_function(container,directory)
manage_directory_permissions(container, directory)
#0f0479fa-7595-4aca-9d3b-f5f0a006cea0