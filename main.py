from flask import Flask,render_template,request,jsonify
import webbrowser
from prediction import Getindex,recomandationEngine
from collections import deque

import pickle


app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
#@app.route('/index')
def hello():

    
    if request.method == "POST": 
       # getting input with name = fname in HTML form 
       first_name = request.form.get("fname") 
       predict=[]

       indx=int(Getindex(first_name))
       if indx>=0:
           print(indx)
           predict=recomandationEngine(indx)
           print(predict)
           print(len(predict))
           size=len(predict)
           
           
       else:
            predict.append('You Enter a Wrong Keyword')
            print(len(predict))
            size=len(predict)

       

       
      
      
       

       

        
      
    


        
    
    #recomandationEngine(indx)
    
    return render_template('index.html',predict=predict,first_name=first_name,size=size )
    
   

if __name__ == "__main__":
    app.run(debug=True)