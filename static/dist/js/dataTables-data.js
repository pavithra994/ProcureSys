/*DataTable Init*/

"use strict"; 

$(document).ready(function() {
	$('#datable_1').DataTable({
		responsive: true,
		autoWidth: false,
		search : {"caseInsensitive" : true},
		language: { search: "",
		searchPlaceholder: "Search",
		sLengthMenu: "_MENU_items"

		}
	});

	$('#datable_2').DataTable({
		responsive: true,
		autoWidth: false,
		search : {"caseInsensitive" : true},
		language: { search: "",
		searchPlaceholder: "Search",
		sLengthMenu: "_MENU_items"

		}
	});

	$('#datable_3').DataTable({
		responsive: true,
		autoWidth: false,
		search : {"caseInsensitive" : true},
		language: { search: "",
		searchPlaceholder: "Search",
		sLengthMenu: "_MENU_items"

		}
	});

	
	var table = $('#datable_5').DataTable({
		responsive: true,
		language: { 
		search: "" ,
		sLengthMenu: "_MENU_Items",
		},
		"bPaginate": false,
		"info":     false,
		"bFilter":     false,
		});
	$('#datable_5 tbody').on( 'click', 'tr', function () {
        if ( $(this).hasClass('selected') ) {
            $(this).removeClass('selected');
        }
        else {
            table.$('tr.selected').removeClass('selected');
            $(this).addClass('selected');
        }
    } );
 
    $('#button').click( function () {
        table.row('.selected').remove().draw( false );
    } );
} );