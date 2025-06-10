import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

#GET istegi
print("Get isteği yapılıyor ..")
get_response = requests.get(f"{BASE_URL}/1")

print ("Durum:",get_response.status_code)
print("Yanıt:",get_response.json(),"\n")

#POST istegi
print("Post isteği yapılıyor ..")
post_data = {
    "title": "Test başlık",
    "body": "Bu bir test mesajıdır.",
    "userId": 1
}
post_response = requests.post(BASE_URL, json=post_data)
print("Durum:", post_response.status_code)
created_post = post_response.json()
print("Yanıt:", created_post, "\n")

#Put isteği
print("Put isteği yapılıyor ..")

updated_post = {
    "id": created_post['id'],
    "title": "Güncellenmiş Başlık",
    "body": "Güncellenmiş içerik",
    "userId": 1
}
put_response = requests.put(f"{BASE_URL}/{created_post['id']}", json=updated_post)
print("Durum:", put_response.status_code)
print("Yanıt:", put_response.json(), "\n")

# 4. DELETE
print(" DELETE isteği yapılıyor...")
delete_response = requests.delete(f"{BASE_URL}/{created_post['id']}")
print("Durum:", delete_response.status_code)
print("Silme işlemi başarılı mı?", delete_response.status_code == 200, "\n")