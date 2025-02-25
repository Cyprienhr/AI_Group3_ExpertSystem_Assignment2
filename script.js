document
  .getElementById("loanForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form from refreshing the page

    // Get form values
    let businessAge = parseInt(document.getElementById("businessAge").value);
    let revenue = parseInt(document.getElementById("revenue").value);
    let loanRequested = parseInt(
      document.getElementById("loanRequested").value
    );
    let collateral = document.getElementById("collateral").value === "true";
    let creditScore = parseInt(document.getElementById("creditScore").value);
    let unpaidLoans = document.getElementById("unpaidLoans").value === "true";
    let defaultRate = parseFloat(document.getElementById("defaultRate").value);
    let registered = document.getElementById("registered").value === "true";

    // Prepare the request data object
    let requestData = {
      businessAge,
      revenue,
      loanRequested,
      collateral,
      creditScore,
      unpaidLoans,
      defaultRate,
      registered,
    };

    // Make the POST request to check eligibility
    fetch("http://localhost:8000/check-eligibility", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(requestData),
    })
      .then((response) => response.json()) // Parse the JSON response
      .then((data) => {
        // Display the result on the page
        document.getElementById("result").textContent = `Result: ${
          data.status
        } - ${data.reason || data.loan_range}`;
      })
      .catch((error) => console.error("Error:", error)); // Log any errors
  });
