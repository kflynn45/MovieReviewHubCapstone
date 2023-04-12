/**
 * Author: Connor Oaks
 * Date: 04-11-2023
 * 
 * This file contains the client side scripting for the title grid display. 
 */

function goToPage(event, action, pageNumber) {
    if(event.which === 13 && !isNaN(pageNumber) && pageNumber >= 1) {
        window.location = `/${action}/page=${pageNumber}` 
    }
}

function resetErrorMessage() {
    $('#paging-error-output').text("") 
}