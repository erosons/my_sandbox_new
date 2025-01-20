var $j = jQuery.noConflict();

// Function to update cell color based on status
function updateCellColor(cell) {
    var prequisisteStatus = cell.innerText.toLowerCase();

  // Check if the status is pending
  if (prequisisteStatus === 'pending') {
    cell.style.backgroundColor = 'yellow';
    } 
  else {
    cell.style.backgroundColor = '';  // Reset background color
  }
}


// Create a MutationObserver to watch for changes in the table
var observer = new MutationObserver(function (mutations) {
    mutations.forEach(function (mutation) {
        // Check if the mutation is a change in the text content of a status cell
        if (mutation.type === 'characterData') {
            var targetNode = mutation.target;
            updateCellColor(targetNode);
        }
    });
});

$j(document).ready(function () {
    // Select all status cells in the table
    var statusCells = document.querySelectorAll('td:nth-child(3)');

    // Iterate over each status cell and start observing changes
    statusCells.forEach(function (statusCell) {
        observer.observe(statusCell, { characterData: true });
        // Update color for the initial state
        updateCellColor(statusCell);
    });
});
