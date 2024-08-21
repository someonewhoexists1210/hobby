hobby_list = ["Reading", "Writing", "Learning languages", "Solving puzzles", "Hiking", "Cycling", "Running", "Rock climbing", "Painting", "Drawing", "Crafting", "Playing musical instruments", "Team sports", "Board games", "Volunteering", "Joining clubs"]
hobbies = {
    "Intellectual/Educational": ["Reading", "Writing", "Learning Languages", "Solving Puzzles"],
    "Physical/Adventurous": ["Hiking", "Cycling", "Running", "Rock climbing"],
    "Creative/Artistic": ["Painting", "Drawing", "Crafting", "Playing Musical Instruments"],
    "Social/Group-Based": ["Team sports", "Board games", "Volunteering", "Joining clubs"]
}
link_exceptions = {
    "Learning languages": "languages", 
    "Solving puzzles": "puzzles", 
    "Playing musical instruments": "music", 
    "Team sports": "teamsports", 
    "Board games": "boardgames", 
    "Joining clubs": "clubs"
}
def suggestHobby(answers):
    hobby_categories = {
        "1": "Intellectual/Educational",
        "2": "Physical/Adventurous",
        "3": "Creative/Artistic",
        "4": "Social/Group-Based"
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
    
    toreturn = []
    for hobby in suggested_hobbies:
        if hobby in link_exceptions.keys():
            toreturn.append({"name": hobby, "link": link_exceptions[hobby]})
            continue
        toreturn.append({"name": hobby, "link": hobby.lower().replace(" ", "_")})
    return toreturn

def all_hobbies():
    toreturn = []
    for hobby in hobby_list:
        if hobby in link_exceptions.keys():
            toreturn.append({"name": hobby, "link": link_exceptions[hobby]})
            continue
        toreturn.append({"name": hobby, "link": hobby.lower().replace(" ", "_")})
    return toreturn

