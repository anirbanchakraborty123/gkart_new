
$(document).ready(function(){ 
        var endpoint = $("#search_form").attr("url_ref_for_autocomplete");
        var search_url= $("#search_form").attr("action");

        $( "#id-search" ).autocomplete({
            
            source: function( request, response ) {

                    var search = $('#id-search').val()
				    console.log(search)
                    console.log(request)

                    $.ajax( {
                        url: endpoint,
                        dataType: "json",
                        data: {
                        search1: search
                        },
                        beforeSend: function(){
                            // Code to run before ajax call
                            console.log("BEFORE SEND");
                        },
                        success: function( data ) {
                            setTimeout(function(){

                                    console.log( data );                           
                                    response($.map(data, function (item) {
                                        //console(item.product_name)
                                        return {
                                            label: item,                                                   
                                        };
                                    }));   
                            },2000);
                        }
                    } );
            },
           
            minLength: 1,
           
            select: function(event,ui){     // ======> select: is used to do some action when a value is selected 
                
                var selectedObj = ui.item;   // For getting the selected object/value from menu
                $('#id-search').val(selectedObj.value)   // For assigning the selected item to the inputbox
                var search2 = $('#id-search').val()  // After assigning the value we need to fetch the value
                console.log(search2)        
                //alert(selectedObj.value);
                window.location.href = search_url+"?id-search="+search2  // Redirecting to the url
                
            }          
        } );
});
