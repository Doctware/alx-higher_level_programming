const add_item = $("#add_item");

add_item.click(function(){
	$("ul.my_list").append("<li>Item</li>");
});
