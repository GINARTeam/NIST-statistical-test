import urllib2
import requests
import json
import thread

########### N THREAD
# N = 2
# url = []
# def thread_get(url_,count,input_f):
#     ticket = requests.get(url_, headers = {'Connection': 'close'}).text

#     if url_ == url[N-1]:
#         for i in range(count - (N - 1)*count / N):
        
#             req = requests.get(('https://test.ginar.io/rng/generate/' + ticket), headers = {'Connection': 'close'})
        
#             print(req.elapsed.total_seconds())

#             response = req.json()
            
#             if response[u'beacon'] == '0xundefined':
#                 print(response)
#             else:
#                 print(response)
#                 beacon = (long(str(response[u'beacon']),16))
#                 input_f.write(format(beacon,'0256b') + '\n')
#                 i += 1
#     else:
#         for i in range(count/N):
            
#             req = requests.get(('https://test.ginar.io/rng/generate/' + ticket), headers = {'Connection': 'close'})

#             print(req.elapsed.total_seconds())

#             response = req.json()
            
#             if response[u'beacon'] == '0xundefined':
#                 print(response)
#             else:
#                 print(response)
#                 beacon = (long(str(response[u'beacon']),16))
#                 input_f.write(format(beacon,'0256b') + '\n')
#                 i += 1

            
#         ticket = str(response[u'sessionKey'])
# def getInput():
#     count = input('Number of requests ( min = 8000 ): ')
#     input_f = open('input.txt','w')
    
    
#     for i in range(N):
#         a = raw_input('Your URL with session-key %d: ' %i)
#         url.append(a)
        
#     for i in range(N):    
#         try:
#             thread.start_new_thread(thread_get,(url[i],count,input_f))
#         except:
#             print ("Error: unable to start thread")
#         finally:
#             pass
# getInput()


################ 1 THREAD
def getInput():
    input_f = open('input.txt','a')
    count = input('Number of requests ( min = 8000 ): ')
    url = raw_input('Your URL with session-key : ' )
    ticket = requests.get(url, headers = {'Connection': 'close'}).text
    for i in range(count):      
        req = requests.get(('https://test.ginar.io/rng/generate/' + ticket), headers = {'Connection': 'close'})
        #req = urllib2.Request('https://test.ginar.io/rng/generate/' + ticket)
        print(req.elapsed.total_seconds())
        #response = urllib2.urlopen(req).json()
        response = req.json()
        if response[u'beacon'] == '0xundefined':
            #print(response)
            i -= 1
        else:
            #print(response)
            beacon = (long(str(response[u'beacon']),16))
            input_f.write(format(beacon,'0256b') + '\n')
            i += 1
        ticket = str(response[u'sessionKey'])

#getInput()











