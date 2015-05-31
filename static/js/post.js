function categoryClick() {
    new Ajax.Request("books.php", 
        {
            method: "GET",
            parameters: {category: this.innerHTML},
            onSuccess: showBooks,
            onFailure: ajaxFailed,
            onException: ajaxFailed
        }
    );
}

function showBooks(ajax) {
    // clear out the list of categories
    while ($("books").firstChild) {
        $("books").removeChild($("books").firstChild);
    }
    
    // add all books from the XML to the page's bulleted list
    var books = ajax.responseXML.getElementsByTagName("book");
    for (var i = 0; i < books.length; i++) {
        var titleNode  = books[i].getElementsByTagName("title")[0];
        var authorNode = books[i].getElementsByTagName("author")[0];
        var title  = titleNode.firstChild.nodeValue;
        var author = authorNode.firstChild.nodeValue;
        var year = books[i].getAttribute("year");
        
        var li = document.createElement("li");
        li.innerHTML = title + ", by " + author + " (" + year + ")";
        $("books").appendChild(li);
    }
}