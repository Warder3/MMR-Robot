import requests
from bs4 import BeautifulSoup

def find_mmr(sum_name):
    sum_name = sum_name

    url = f'https://na.whatismymmr.com/api/v1/summoner?name={sum_name}'

    # Load webpage content
    request = requests.get(url)

    # Convert to a beautiful soup object
    soup = BeautifulSoup(request.content, 'lxml')

    text = soup.find('p').text
    if (len(text) < 100):
        return(f'Summoner {sum_name}: You have no recent SOLO games to analyze. Get out on the rift!')

    mmr = ''
    rank = soup.find('p').b.text

    mmr_curr = text.find('ranked') + 15

    while (text[mmr_curr].isdigit()):
        mmr += text[mmr_curr]
        mmr_curr += 1
    
    msg = f'''Summoner {sum_name}:
Well Done! Your MMR is approximately {mmr}. This MMR is sililar to those {rank}.'''

    return(msg)