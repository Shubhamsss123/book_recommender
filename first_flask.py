import flask
import pickle
from flask import Flask,render_template,request
import pandas as pd
import numpy as np
from flask_swagger import swagger
app=Flask(__name__)
app.config['SWAGGER_UI_ENABLED'] = True
swagger_ui=swagger(app)

@app.route('/r', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         return 'Your name is {} and your email is {}'.format(name, email)
#     else:
#         return render_template('user.html')


# app.route('/p',methods=['GET','POST'])
def func():
    if request.method == 'POST':
        name = request.form['content']
        
        with open('table.pkl','rb') as f :
            table=pickle.load(f)
        with open('cos_data.pkl','rb') as f :
            cos=pickle.load(f)

        # return 'inside p'
        def book_data(title):
            df_books=pd.read_csv('Books.csv')
            arr=df_books[df_books['Book-Title']==title].iloc[:1,:].values
        #     print(arr)
        #     return arr
            arr=arr[0]
            return [arr[2],arr[3],arr[7]]
        
        def find_similar(book):
        
            index=np.where(table.index==book)[0][0]
            
            s=[i[0] for i in sorted(list(enumerate(cos[index])),key=lambda x:x[1],reverse=True)[1:4]]
            
            return [book_data(table.index[x]) for x in s]
        data=find_similar(name)
        return render_template('new.html',data=data)
        
    else:
        return render_template('user.html')
    
    return 

# swagger_ui = swagger(app)
@app.route('/k')
def ch():

    return 'hi'
@app.route("/")
def hello_world():

    # df=pd.read_csv('Books.csv')

    # return {'shape of file':str(df.shape[0])}
    # return 
    with open('top50.pkl','rb') as f:
        top50=pickle.load(f)
    
    # return {'shape of file':str(top50.shape[0])}
    # print(top50.shape)
    data={
        'title':top50['title'].values,
        'author':top50['author'].values,
        'year':top50['year'].values,
        'rating':top50['rating'].values,
        'url':top50['url'].values

    }
    return render_template('index.html',data=data)

app.route('/hi')
def check():

    return 'it works'
