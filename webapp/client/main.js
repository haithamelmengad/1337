$(document).ready(() => {
	// handle click on submit button
	$("#buttonsub").on("click", (event) => {
		
		// if input matches condition, prevent post then populate and unhide modal

		if($("#target").val() === "Fen is a 1337 H4X0R, " || $("#target").val() === "Fen is a 1337 H4X0R"){
			event.preventDefault();
			$("#title").text("Alright, alright, alright");
			$("#result").text("Correct");
			$("#result").toggleClass("red");
			$("#result-modal").modal("toggle");
		} 
		if($("#target").val()  === "Fen is not a 1337 H4X0R, " || $("#target").val() === "Fen is not a 1337 H4X0R"){
			event.preventDefault();
			$("#title").text("YOU FAILED");
			$("#result").text("Incorrect");
			$("#result").toggleClass("green");
			$("#result-modal").modal("toggle");
		}
    
	});

	// handle modal close --> submit form to post to "/" endpoint and save to db
	$("#result-modal").on("hidden.bs.modal", () => {
		$("#innerform").trigger("submit");
	});
});