const add_item = $("#add_item");

add_item.click(function(){
	$("ul.my_list").add("<li>Item</li>");
});
