import time

from steampy.guard import generate_one_time_code
# def getcode(share):
#     shared_secret = share
#     one_time_authentication_code = generate_one_time_code(shared_secret)
#     return one_time_authentication_code
#
# print(getcode("F9CSJDYQtnvfbR6Ypoo81YWfMkY="))
from steampy.client import SteamClient

steam_client = SteamClient('MY_API_KEY')
one_time_authentication_code = generate_one_time_code("F9CSJDYQtnvfbR6Ypoo81YWfMkY=")
proxy123 = "193.58.168.68:1051:Mv47Xq@OLwHrOlBug"
steam_client._session.proxies = {"http": f"http://{proxy123}",
                                 "https": f"https://{proxy123}"
                                 }
steam_client.login('facnandcapleo1986', 'ZhlBXiXy', 'steamguard.txt')
# time.sleep(5)
# steam_client.logout()

# print(steam_client)
is_session_alive = steam_client.is_session_alive()
print(is_session_alive)
# # steam_client.logout()
# is_ssq = steam_client.is_session_alive()
# print(is_ssq)
