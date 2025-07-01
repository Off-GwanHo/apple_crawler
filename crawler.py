from bs4 import BeautifulSoup

def count_apples(filename):
  try:
    with open(filename,'r',encoding='utf-8') as file:
      html_content = file.read()
  except FileNotFoundError :
    print('파일을 찾을수없음')
    return
  except Exception as e :
    print(f'오류 :{e}')
    return
  
  soup = BeautifulSoup(html_content,'html.parser')
  text = soup.get_text()
  sentences = text.replace('?','.').replace('!','.').split('.')

  apple_counts = text.count('사과')
  apple_sentences = []

  for s in sentences:
    if '사과' in s:
      apple_sentences.append(s.strip())

  return apple_counts, apple_sentences

if __name__ =='__main__':
  result = count_apples('apple_website.html')
  count , sentences =result
  print(f'총 발견한 사과는 {count}개 입니다.\n')

  print('사과가 포함된 문장: ')
  for i, s in enumerate(sentences, 1):
    print(f'{i}.{s}')