 // Function to make an AJAX request to your API
function callAPI() {
    var category = 'success'
    $.ajax({
        method: 'GET',
        url: 'https://api.api-ninjas.com/v1/quotes?category=' + category,
        headers: { 'X-Api-Key': 'uiWEnqFwzOHBu984T2GHyg==aB5sTLsHsFfJ9vpQ'},
        contentType: 'application/json',
        success: function(result) {
            console.log(result[0].quote);
            console.log(result[0].author);
            document.getElementById("quote").innerHTML = `"${result[0].quote}"`
            document.getElementById("author").innerHTML = `- ${result[0].author}`
        },
        error: function ajaxError(jqXHR) {
            console.error('Error: ', jqXHR.responseText);
        }
});
}

// Call the API function when the page loads
window.addEventListener('load', callAPI);
// Call the API function when the user refreshes the page
window.addEventListener('beforeunload', callAPI);

// // Hide delete button until user clickes complete goal
// const del = document.getElementById('delete')
// window.addEventListener('load', () => {
//     del.style.display = 'none'
//   });

// // Hide image until user clickes complete goal
// const reward = document.getElementById('reward1')
// window.addEventListener('load', () => {
//     reward.style.display = 'none'
//   });

function showReward(goal_id){
    console.log(goal_id)
    let toggle = document.getElementById(goal_id)
    console.log(toggle)

    if(toggle.style.display === "none"){
        toggle.style.display = "block";
    }
    else{
        toggle.style.display = "none";
    }

    let del = document.getElementById(goal_id + ' delete')

    if(del.style.display === "none"){
        del.style.display = "inline-block";
    }
    else{
        del.style.display = "none";
    }

    let up = document.getElementById(goal_id + ' update')

    if(up.style.display === "none"){
        up.style.display = "inline-block";
    }
    else{
        up.style.display = "none";
    }

    // hides the complete button
    let com = document.getElementById(goal_id + ' complete')

    if(com.style.display === "none"){
        com.style.display = "inline-block";
    }
    else{
        com.style.display = "none";
    }

    let goal = goal_id + "reward"
    console.log(goal)
    let reward = document.getElementById(goal_id + " reward")

    if(reward.style.display === "none"){
        reward.style.display = "block";
    }
    else{
        reward.style.display = "none";
    }


// exploding letters
const rand = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;

const enhance = id => {
  const element = document.getElementById(id),
        text = element.innerText.split("");
  
  element.innerText = "";
  
  text.forEach((value, index) => {
    const outer = document.createElement("span");
    
    outer.className = "outer";
    
    const inner = document.createElement("span");
    
    inner.className = "inner";
    
    inner.style.animationDelay = `${rand(-5000, 0)}ms`;
    
    const letter = document.createElement("span");
    
    letter.className = "letter";
    
    letter.innerText = value;
    
    letter.style.animationDelay = `${index * 1000 }ms`;
    
    inner.appendChild(letter);    
    
    outer.appendChild(inner);    
    
    element.appendChild(outer);
  });
}

enhance(goal_id + " explode");



}

/* Cool rapid letter change effect*/

const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

let interval = null;

document.getElementById("goal-header").onmouseover = event => {  
  let iteration = 0;
  
  clearInterval(interval);
  
  interval = setInterval(() => {
    event.target.innerText = event.target.innerText
      .split("")
      .map((letter, index) => {
        if(index < iteration) {
          return event.target.dataset.value[index];
        }
      
        return letters[Math.floor(Math.random() * 26)]
      })
      .join("");
    
    if(iteration >= event.target.dataset.value.length){ 
      clearInterval(interval);
    }
    
    iteration += 1 / 3;
  }, 30);
}
