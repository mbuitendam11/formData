 // Ingredient section Recipe Form

 var ingredientCounter = 2;
		
 $("#addIngredient").click(function () {
             
     if(ingredientCounter>10){
             alert("Only 10 textboxes allow");
             return false;
     }   
         
     var newTextBoxDiv = $(document.createElement('div'))
         .attr("id", 'TextBoxDiv' + ingredientCounter)
         .attr("class", 'col col-md-2 form-floating');
                 
     newTextBoxDiv.after().html(
        '<input type="email" class="form-control" \
        placeholder="floatinginput" id="floatinginput" \
        name="floatinginput[]" class="px-2"> \
        </input><label for="floatinginput" class="">Ingredient ' + ingredientCounter + '</label>');
             
     newTextBoxDiv.appendTo("#IngredientBoxesGroup");
 
                 
     ingredientCounter++;
 });
 
 $("#removeIngredient").click(function () {
     if(ingredientCounter==2){
         alert("You cannot remove any more ingredients.");
         return false;
     }   
         
     ingredientCounter--;
             
         $("#TextBoxDiv" + ingredientCounter).remove();
             
 });