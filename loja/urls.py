from django.shortcuts import render
from django.urls import path
from django.contrib import admin
import requests
from django.http import JsonResponse
import json
from datetime import datetime, timedelta
import socket
import ipaddress
#                               __          ________    _________        ________
#  --------   .  |     /       /  \        |        \  |         \     /          \
#         /   |  |    /       /    \       |        /  |          \   |            |
#        /    |  |   /       /      \      |       /   |           \  |            |
#       /     |  |  /       /--------\     |------\    |            \ |            |
#      /      |  |   \     /          \    |       \   |            / |            |
#     /       |  |    \   /            \   |        \  |           /  |            |
#    /________|  |     \ /              \  |         \ |__________/    \__________/


# def calcular_data_12_dias_uteis():
#     dias_uteis = 0
#     data_atual = datetime.now()
#     data_futura = data_atual
    
#     while dias_uteis < 12:
        
#         data_futura += timedelta(days=1)
        
        
#         if data_futura.weekday() < 5:  
#             dias_uteis += 1
    
    
#     return data_futura

# def formatar_data_por_extenso(data):
    
#     meses = {
#         1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 
#         5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 
#         9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'
#     }
    
    
#     dia = data.day
#     mes = meses[data.month]
#     data_formatada = f'{dia} de {mes}'
    
#     return data_formatada


    
    






# def obter_endereco_ipv6_local():
#     try:
        
#         s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
#         s.connect(("ipv6.google.com", 80))  
#         endereco_ipv6 = s.getsockname()[0]
#         s.close()
#         return endereco_ipv6
#     except socket.error:
#         return None

# def get_location(request):

#     ip_address = obter_endereco_ipv6_local()

#     try:
#         url = f"https://ipinfo.io/{ip_address}/json"
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()

#         context = {
#             'data': data
#         }
       
        

#         return context

#     except requests.exceptions.RequestException as e:
    
#         context = {
#             'data': None
#         }
        
#         return context








# # #######################3333333###################


# def buscar_endereco_por_cep(cep):
#     url = f'https://viacep.com.br/ws/{cep}/json/'
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return None


# def carregar_produtos():
#     with open('infos.json', 'r', encoding='utf-8') as file:
#         produtos = json.load(file)
        
#         for produto in produtos:
#             produto['id'] = int(produto['id'])
#     return produtos

# produtos = carregar_produtos()




# def produto_detalhes(request, produto_id=None):
    
#     data_12_dias_uteis = calcular_data_12_dias_uteis()
    
    
#     data_formatada = formatar_data_por_extenso(data_12_dias_uteis)
    

#     diaMes = {
#         'data_formatada': data_formatada,
#     }
#     ipv6 = get_location(request)

#     if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        
#         cep = request.POST.get('cep_input')
#         endereco = buscar_endereco_por_cep(cep)
#         if endereco:
            
#             return JsonResponse({'localidade': endereco.get('localidade'), 'uf': endereco.get('uf')})
#         else:
#             return JsonResponse({'error': 'Endereço não encontrado'}, status=404)
#     else:
       
        
#         if produto_id is not None:
#             produto = next((p for p in produtos if p['id'] == produto_id), None)
#             if produto is None:
#                 return render(request, '404.html')  
#             return render(request, 'product.html', {'ipv6':ipv6,'diaMes':diaMes,'produto': produto, 'todos_os_produtos': json.dumps(produtos)})
#         else:
            
#             return render(request, 'product.html', {'ipv6':ipv6,'diaMes':diaMes,'produto': None, 'todos_os_produtos': json.dumps(produtos)})
        
# def pag_index(request,produto_id=None):
     
#     data_12_dias_uteis = calcular_data_12_dias_uteis()
    
    
#     data_formatada = formatar_data_por_extenso(data_12_dias_uteis)
    
    
#     diaMes = {
#         'data_formatada': data_formatada,
#     }
#     ipv6 = get_location(request)

#     if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        
#         cep = request.POST.get('cep_input')
#         endereco = buscar_endereco_por_cep(cep)
#         if endereco:
            
#             return JsonResponse({'localidade': endereco.get('localidade'), 'uf': endereco.get('uf')})
#         else:
#             return JsonResponse({'error': 'Endereço não encontrado'}, status=404)
#     else:
       
        
#         if produto_id is not None:
#             produto = next((p for p in produtos if p['id'] == produto_id), None)
#             if produto is None:
#                 return render(request, '404.html')  
#             return render(request, 'index.html', {'ipv6':ipv6,'diaMes':diaMes,'produto': produto, 'todos_os_produtos': json.dumps(produtos)})
#         else:
            
#             return render(request, 'index.html', {'ipv6':ipv6,'diaMes':diaMes,'produto': None, 'todos_os_produtos': json.dumps(produtos)})
    

       
# def pag_contato(request,produto_id=None):
     
#     data_12_dias_uteis = calcular_data_12_dias_uteis()
    
    
#     data_formatada = formatar_data_por_extenso(data_12_dias_uteis)
    
    
#     diaMes = {
#         'data_formatada': data_formatada,
#     }
   

#     if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        
        
#         cep = request.POST.get('cep_input')
#         endereco = buscar_endereco_por_cep(cep)
#         if endereco:
            
#             return JsonResponse({'localidade': endereco.get('localidade'), 'uf': endereco.get('uf')})
#         else:
#             return JsonResponse({'error': 'Endereço não encontrado'}, status=404)
#     else:
        
        
       
        
#         if produto_id is not None:
#             produto = next((p for p in produtos if p['id'] == produto_id), None)
#             if produto is None:
                
#                 return render(request, '404.html')  
#             return render(request, 'contact.html', {'diaMes':diaMes,'produto': produto, 'todos_os_produtos': json.dumps(produtos)})
#         else:
            
            
#             return render(request, 'contact.html', {'diaMes':diaMes,'produto': None, 'todos_os_produtos': json.dumps(produtos)})
    
      
# def pag_sacola(request,produto_id=None):
     
#     data_12_dias_uteis = calcular_data_12_dias_uteis()
    
    
#     data_formatada = formatar_data_por_extenso(data_12_dias_uteis)
    
    
#     diaMes = {
#         'data_formatada': data_formatada,
#     }
   

#     if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        
        
#         cep = request.POST.get('cep_input')
#         endereco = buscar_endereco_por_cep(cep)
#         if endereco:
            
#             return JsonResponse({'localidade': endereco.get('localidade'), 'uf': endereco.get('uf')})
#         else:
#             return JsonResponse({'error': 'Endereço não encontrado'}, status=404)
#     else:
        
        
       
        
#         if produto_id is not None:
#             produto = next((p for p in produtos if p['id'] == produto_id), None)
#             if produto is None:
                
#                 return render(request, '404.html')  
#             return render(request, 'sacola.html', {'diaMes':diaMes,'produto': produto, 'todos_os_produtos': json.dumps(produtos)})
#         else:
            
            
#             return render(request, 'sacola.html', {'diaMes':diaMes,'produto': None, 'todos_os_produtos': json.dumps(produtos)})
    
# def sobre_loja(request):
#     return render(request,'sob_loja.html')

# def poli_privac(request):
#     return render(request,'polipri.html')

# def poli_entreg(request):
#     return render(request,'polientre.html')

def troc_devolu(request):
    return render(request,'trodevo.html')


            
       


urlpatterns = [
    # path('produto/<int:produto_id>/', produto_detalhes, name='produto_detalhes'),
    # path( '', pag_index ,name='pag_index'),
    # path('sacola/', pag_sacola ,name='sacola'),
    # path('contato/', pag_contato ,name='contato'),
    # path('sobre/',sobre_loja ,name='sobre_loja' ),
    # path('privacidade/',poli_privac ,name='poli_privac' ),
    # path('entrega/',poli_entreg ,name='poli_entreg'),
    path('devolucao/',troc_devolu ,name='troc_devolu')
]

