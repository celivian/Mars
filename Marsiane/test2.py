from requests import post, get, delete
print('ПРОВЕРКА get')
print('---')
print(get('http://127.0.0.1:8080/api/v2/user').json())
print(get('http://127.0.0.1:8080/api/v2/user/3243').json())
print(get('http://127.0.0.1:8080/api/v2/user/reerg').json())
print(get('http://127.0.0.1:8080/api/v2/user/13').json())
print('ПРОВЕРКА post')
print('---')
print(post('http://127.0.0.1:8080/api/v2/user', json={'surname': 'RISLWY123',
                                                      'name': 'Посдаить дерево123',
                                                      'age': 9,
                                                      'position': 'medic',
                                                      'speciality': 'True',
                                                      'address': '123',
                                                      'email': 'efreg@fkf.u',
                                                      'hashed_password': '123'}).json())
print(post('http://127.0.0.1:8080/api/v2/user', json={'surname': 'RISLWY',
                                                      'name': 'Посдаить дерево'}).json())
print(post('http://127.0.0.1:8080/api/v2/user', json={}).json())
print('ПРОВЕРКА delete')
print('---')
print(delete('http://127.0.0.1:8080/api/v2/user/11').json())
print(delete('http://127.0.0.1:8080/api/v2/user').json())
print(delete('http://127.0.0.1:8080/api/v2/user/21421').json())
print(delete('http://127.0.0.1:8080/api/v2/user/wefwe').json())
