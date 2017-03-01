from flask import Flask , render_template , jsonify ,request
from flask_wtf import Form
from wtforms import RadioField
from wtforms.validators import DataRequired
import predictor




app = Flask(__name__)
app.config.from_object('config')

class SurveyForm(Form):

    q1  = RadioField(label='1. When something good happens to me, I have people who I like to share the good news with.',
                    choices=[('2','Almost always'),('1','Very often'),('0','Often'),('-1','Sometimes'),('-2','Almost never')],
                    validators =[DataRequired()],)
    q2  = RadioField(label='2. I finish whatever I begin.',
                    choices=[('2','Almost always'),('1','Very often'),('0','Often'),('-1','Sometimes'),('-2','Almost never')],
                    validators =[DataRequired()])

    q3  = RadioField(label='3. When I do an	activity, I	enjoy it so much that I	lose track of time.',
                    choices=[('2','Almost always'),('1','Very often'),('0','Often'),('-1','Sometimes'),('-2','Almost never')],
                    validators =[DataRequired()])

    q4  = RadioField(label='4. I get completely absorbed in what I am doing.',
                    choices=[('2','Almost always'),('1','Very often'),('0','Often'),('-1','Sometimes'),('-2','Almost never')],
                    validators =[DataRequired()])

    q5  = RadioField(label='5. I am optimistic about my future.',
                    choices=[('2','Almost always'),('1','Very often'),('0','Often'), ('-1','Sometimes'),('-2','Almost never')],
                    validators =[DataRequired()])

    q6  = RadioField(label='6. I keep at my collegework until I	am	done with it.',
                     choices=[('2','Almost always'),('1','Very often'),('0','Often'), ('-1','Sometimes'),('-2','Almost never')],
                     validators =[DataRequired()])

    q7  = RadioField(label='7. When I have a problem, I have someone who will be there for me.',
                     choices=[('2','Almost always'),('1','Very often'),('0','Often'),('-1','Sometimes'),('-2','Almost never')],
                     validators =[DataRequired()])

    q8  = RadioField(label='8. In uncertain times, I expect the	best.',
                     choices=[('2','Almost always'),('1','Very often'),('0','Often'),('-1','Sometimes'),('-2','Almost never')],
                     validators =[DataRequired()])

    q9  = RadioField(label='9. There are people in my life who really care about me.',
                     choices=[('2','Almost always'),('1','Very often'),('0','Often'),('-1','Sometimes'),('-2','Almost never')],
                     validators =[DataRequired()])

    q10 = RadioField(label='10. I think good things are going to happen to me.',
                     choices=[('2','Almost always'),('1','Very often'),('0','Often'),('-1','Sometimes'),('-2','Almost never')],
                     validators =[DataRequired()])

    q11 = RadioField(label='11. I have friends that I really care about.',
                     choices=[('2','Almost always'),('1','Very often'),('0','Often'), ('-1','Sometimes'),('-2','Almost never')],
                     validators =[DataRequired()])

    q12 = RadioField(label='12. Once I make a plan to get something done, I stick to it.',
                     choices=[('2','Almost always'),('1','Very often'),('0','Often'),('-1','Sometimes'),('-2','Almost never')],
                     validators =[DataRequired()])

    q13 = RadioField(label='13. I believe that things will work out, no matter how difficult they seem.',
                     choices=[('2','Almost always'),('1','Very often'),('0','Often'), ('-1','Sometimes'),('-2','Almost never')],
                     validators =[DataRequired()])

    q14 = RadioField(label='14. I work hard.',
                     choices=[('2','Almost always'),('1','Very often'),('0','Often'),('-1','Sometimes'),('-2','Almost never')],
                     validators =[DataRequired()])

    q15 = RadioField(label='15. I have a lot of fun.',
                     choices=[('2','Almost always'),('1','Very often'),('0','Often'), ('-1','Sometimes'),('-2','Almost never')],
                     validators =[DataRequired()])

@app.route('/',methods = ['POST' ,'GET'])
def index():
    form = SurveyForm()
    if form.validate_on_submit():
        print (request.form.get('q1'))
        thisform_input= [int(form.q1.data), int(form.q2.data),int(form.q3.data),int(form.q4.data),int(form.q5.data),
                         int(form.q6.data),int(form.q7.data),int(form.q8.data),int(form.q9.data),int(form.q10.data),
                         int(form.q11.data),int(form.q12.data),int(form.q13.data),int(form.q14.data),int(form.q15.data)]

        op = predictor.mentalhealthPredictor().predict(thisform_input)
        if(op==2):
            result ='Optimistic and happy with life'
        elif(op==1):
            result ='Unaffected about life'
        else:
            result = 'Mentally distressed'

        print thisform_input
        return jsonify(result=result)
    else:
        return render_template('theForm.html', form = form)


if __name__ == '__main__':
    app.run(debug=True)
