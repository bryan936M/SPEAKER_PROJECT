"""
VIEWS CONTAINER
"""
from django.shortcuts import render

# Create your views here.

SPEAKERS = [
  {
    "id": 1,
    "name": 'Tyler Bennett',
    "topic": 'IT Industry',
    "city": 'New York City',
    "country": 'USA',
    "active": True,
  },
  {
    "id": 2,
    "name": 'Emma Thompson',
    "topic": 'Artificial Intelligence',
    "city": 'London',
    "country": 'UK',
    "active": True,
  },
  {
    "id": 3,
    "name": 'Hiroshi Tanaka',
    "topic": 'Robotics',
    "city": 'Tokyo',
    "country": 'Japan',
    "active": False,
  },
  {
    "id": 4,
    "name": 'Maria Lopez',
    "topic": 'Marketing Strategies',
    "city": 'Madrid',
    "country": 'Spain',
    "active": True,
  },
  {
    "id": 5,
    "name": 'Alexandre Dubois',
    "topic": 'Blockchain Technology',
    "city": 'Paris',
    "country": 'France',
    "active": True,
  }
]


def create_speaker(request):
    """add a speaker"""
    return render(request, 'NewSpeaker.html', {})

def display_speakers(request):
    """show complete list of speakers"""
    context = {
      'speakers': SPEAKERS
    }
    return render(request, 'home.html', context)

def update_speaker(request, speaker_id):
    """update a speaker's details"""
    for speaker in SPEAKERS:
        if speaker.get('id') == speaker_id:
            return render(request, 'UpdateSpeaker.html', {"speaker": speaker})

def delete_speaker(request, speaker_id):
    """remove a speaker"""
    for speaker in SPEAKERS:
        if speaker.get('id') == speaker_id:
            return render(request, 'deleteSpeaker.html', {"speaker": speaker})
