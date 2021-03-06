var orgs;
var municipio;

$(document).ready(function(){
    $("#id_departamento, #id_municipio, #id_organizacion").html('');
    var pais = $("#id_pais").multiselect({
        noneSelectedText: 'Seleccione el pais',
        selectedText: '# seleccionados',
        minWidth: 200,
        beforeclose: function(event, ui){
            var selectos = $("#id_pais").multiselect("getChecked").map(function(){
                return this.value;
            }).get();
            if(selectos.length!=0){
                $.getJSON('/ajax/depas-groups/?ids='+selectos.join(","), function(data){
                    $('#id_departamento').html('');
                    if(data){
                        $.each(data, function(i, item){
                            $.each(item, function(j, item2){
                                var group = $('<optgroup></optgroup>').attr('label', j);
                                $.each(item2, function(k, item3){
                                    $('<option></option>').val(item3.id).html(item3.nombre).appendTo(group);
                                });
                                group.appendTo(departamento);
                            });
                            departamento.multiselect('refresh');
                        });
                    }
                });
                departamento.multiselect("enable");
            }else{
                departamento.multiselect("disable");
                orgs.multiselect("disable");
                orgs.multiselect("disable");
            }
        }
    });	
    var departamento = $("#id_departamento").multiselect({
        noneSelectedText: 'Todos los departamentos',
        selectedText: '# seleccionados',
        minWidth: 200,
        beforeclose: function(event, ui){
            var selectos = $("#id_departamento").multiselect("getChecked").map(function(){
                return this.value;
            }).get();
            if(selectos.length!=0){
                $.getJSON('/ajax/muni/?ids='+selectos.join(","), function(data){
                    $('#id_municipio').html('');
                    if(data){
                        $.each(data, function(i, item){
                            $.each(item, function(j, item2){
                                var group = $('<optgroup></optgroup>').attr('label', j);
                                $.each(item2, function(k, item3){
                                    $('<option></option>').val(item3.id).html(item3.nombre).appendTo(group);
                                });
                                group.appendTo(municipio);
                            });
                            municipio.multiselect('refresh');
                        });
                        municipio.multiselect("enable");
                    }
                });
                $.getJSON('/ajax/orgs/?ids='+selectos.join(","), function(data){
                    $("#id_organizacion").html('');
                    if(data){
                        $.each(data, function(i, item){
                            $('<option></option>').val(item.id).html(item.nombre_corto).appendTo(orgs)
                        });
                        orgs.multiselect('refresh');
                        orgs.multiselect("enable");
                    }
                });
            }else{
                orgs.multiselect("disable");
                municipio.multiselect("disable");
            }
        }
    });
	
    municipio = $("#id_municipio").multiselect({
        noneSelectedText: 'Todos los municipios',
        selectedText: '# seleccionados',
        minWidth: 200
    });
    EnableOrganizacion();
    departamento.multiselect("disable");
    orgs.multiselect("disable");
    municipio.multiselect("disable");	
});

function EnableOrganizacion(){
    $("#id_organizacion").html("");
    orgs = $("#id_organizacion").multiselect({
        noneSelectedText: 'Todas las organizaciones',
        selectedText: '# seleccionados',
        minWidth: 200,
        beforeclose: function(event, ui){
            var selectos = $("#id_organizacion").multiselect("getChecked").map(function(){
                return this.value;
            }).get();
            if(selectos.length!=0){
                $.getJSON('/ajax/muni/?orgs='+selectos.join(","), function(data){
                    $('#id_municipio').html('');
                    if(data){
                        $.each(data, function(i, item){
                            $('<option></option>').val(item.id).html(item.nombre).appendTo(municipio)
                            municipio.multiselect('refresh');
                        });
                    }
                });
            }else{
                var selectos1 = $("#id_departamento").multiselect("getChecked").map(function(){
                    return this.value;
                }).get();
                if(selectos1.length!=0){
                    $.getJSON('/ajax/muni/?ids='+selectos1.join(","), function(data){
                        $('#id_municipio').html('');
                        if(data){
                            $.each(data, function(i, item){
                                $.each(item, function(j, item2){
                                    var group = $('<optgroup></optgroup>').attr('label', j);
                                    $.each(item2, function(k, item3){
                                        $('<option></option>').val(item3.id).html(item3.nombre).appendTo(group);
                                    });
                                    group.appendTo(municipio);
                                });
                                municipio.multiselect('refresh');
                            });
                        }
                    });
                    municipio.multiselect("enable");
                }else{
                    orgs.multiselect("disable");
                    municipio.multiselect("disable");
                }
            }
        }
    });
}