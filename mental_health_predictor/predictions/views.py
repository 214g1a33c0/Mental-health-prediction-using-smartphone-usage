from django.shortcuts import render
import joblib
from .forms import UsageDataForm

def index(request):
    prediction_result = None
    user_input = None
    if request.method == 'POST':
        form = UsageDataForm(request.POST)
        if form.is_valid():
            model = joblib.load('mental_health_model.pkl')
            user_data = form.cleaned_data
            user_input = {
                'user_id': user_data['user_id'],
                'screen_time': user_data['screen_time'],
                'call_logs': user_data['call_logs'],
                'message_frequency': user_data['message_frequency']
            }
            features = [
                user_data['screen_time'],
                user_data['call_logs'],
                user_data['message_frequency']
            ]
            prediction = model.predict([features])
            prediction_result = 'High risk' if prediction[0] else 'Low risk'
    else:
        form = UsageDataForm()

    return render(request, 'index.html', {'form': form, 'prediction_result': prediction_result, 'user_input': user_input})
