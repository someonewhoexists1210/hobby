def suggestHobby(answers):
    hobby_categories = {
        "1": "Intellectual/Educational",
        "2": "Physical/Adventurous",
        "3": "Creative/Artistic",
        "4": "Social/Group-Based"
    }

    hobbies = {
        "Intellectual/Educational": ["Reading", "Writing", "Learning languages", "Solving puzzles"],
        "Physical/Adventurous": ["Hiking", "Cycling", "Running", "Rock climbing"],
        "Creative/Artistic": ["Painting", "Drawing", "Crafting", "Playing musical instruments"],
        "Social/Group-Based": ["Team sports", "Board games", "Volunteering", "Joining clubs"]
    }
    ans = []
    for answer in answers:
        a = int(answer) % 4
        ans.append(a if a != 0 else 4)

    scores = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0
    }
    for i in ans:
        scores[str(i)] += 1
    
    max_score = max(scores.values())
    max_categories = [k for k, v in scores.items() if v == max_score]
    suggested_hobbies = []
    for category in max_categories:
        suggested_hobbies.extend(hobbies[hobby_categories[category]])
    
    return suggested_hobbies

