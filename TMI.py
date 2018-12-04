import sys, os, re, csv, math, codecs, numpy as np
sys.path.append('../Python36')
sys.path.append('../Python36/Scripts')
sys.path.append('../Python36/Lib/site-packages')
import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences


EMBEDDING_FILE='./data/glove.6B.50d.txt'
TRAIN_DATA_FILE='./data/train.csv'
TEST_DATA_FILE='C:/Users/admin/Downloads/reply.csv'
SUBMISSION_FILE='./data/submission.csv'
MODEL_WEIGHTS_FILE = './toxic_model.h5'


# In[25]:


embed_size = 50 # 단어를 몇 차원으로 임베딩할 것인가(how many dimensions use to embed word?) 
max_features = 20000 # 몇개의 단어를 주요한 특징으로 볼 것인가(How many words will be the main feature?) 
maxlen = 100 # 한 comment에서 가져올 수 있는 단어의 최대 갯수(The maximum number of words a comment can get?)


# In[26]:


train = pd.read_csv(TRAIN_DATA_FILE)
test = pd.read_csv(TEST_DATA_FILE)


print("모델이 비속어 처리중...")
list_sentences_train = train["comment_text"].fillna("_na_").values # comment_text만 가져와서 fillna를 통해 nan를 거른다.
                                                                   # Just import comment_text and filter nan through fillna.
list_classes = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"] # 사용할 컬럼들(to use columns)
y = train[list_classes].values # labels of comment_text
list_sentences_test = test["comment_text"].fillna("_na_").values # Do the same things for test_data


tokenizer = Tokenizer(num_words=max_features) # max_features 만큼의 단어를 Tokenize하기 위한 틀 생성.
                                              # Create a frame to Tokenize words as many as max_features.
tokenizer.fit_on_texts(list(list_sentences_train)) # just fit
list_tokenized_train = tokenizer.texts_to_sequences(list_sentences_train) # Tokenize(Transform word into number)
list_tokenized_test = tokenizer.texts_to_sequences(list_sentences_test) # Tokenize(Transform word into number)


X_te = pad_sequences(list_tokenized_test, maxlen=maxlen) # do the same thing


from keras.models import load_model
model = load_model('toxic_model.h5')

# ## Predict result

y_test = model.predict([X_te], batch_size=1024, verbose=1) # model에 test data를 넣고 예측
sample_submission = pd.read_csv('C:/Users/admin/Downloads/sample_submission.csv') # 예측값을 저장할 csv파일
sample_submission[list_classes] = y_test # csv에 저장할 값을 설정
sample_submission.to_csv('./data/submission.csv', index=False) # csv파일에 저장

##차단중...

print("차단중...")

list=[]
def Find(data):
      # list=[]
      l=len(data)
      # print(len(data))
      for i in range(1,l):
          for j in range(1,7):
              if float(data[i][j])>0.8:
                  # print(data[i][0]+"번째 댓글을 차단해야함")
                  global list
                  list.append(data[i][0])
      # print(list)





with open(SUBMISSION_FILE,'r')as f:

    data=[]
    reader_csv =csv.reader(f,delimiter=',')
    for row in reader_csv:
        data.append(row)
    Find(data)



with open(TEST_DATA_FILE,'r')as f:
    # reader_csv =csv.reader(f,delimiter=',')
    # for row in reader_csv:
    #     print(row)
    file = codecs.open(TEST_DATA_FILE,'r',encoding='utf-8')
    s = file.read()
    # print(s)
    while s.find("  ")!=-1:
        s=s.replace("  "," ")

    text = s.split('\n')
    text[0]=""
    for i in range(len(text)):
        for j in range(len(list)):
            if(i==int(list[j])):
                text[i]=str(i)+", 차단된 댓글입니다."

    print('\n\n'.join(text))


os.system('Pause')
