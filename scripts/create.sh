curl -H 'user_id: 1' localhost:5000/words -X POST -d ' { "user_id" : "1", "word": "apple", "entered_at": "2019-05-11T12:00:00" } ' -H 'content-type: application/json'
