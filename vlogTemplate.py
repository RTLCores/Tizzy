vlogTemplate = """/*
    Auto Generated by Tizzy
    $version
    =======================
    File:           $filename
    Generated on:   $creation_date

    $title
*/
`timescale 1ns / 100ps
`ifndef D
    `define D #1
`endif


module $module_name (
    input   wire clock,
    input   wire reset,
$inputs
    output  reg [$msb:$lsb] state,
    output  reg [$msb:$lsb] state_next
);

/* State parameters for 1-hot encoding */
/* These parameters are indexes to the state reg */
`include "$include_file"

/* Next State Logic */
always @(*) begin
    state_next = $range'b0;
    case (1'b1)
$next_state_logic
    endcase
end

/* State Generator */
always @(posedge clock or posedge reset)
    if(reset) begin
$state_generator
    end
    else
        state <= `D state_next;
endmodule

/*
To reproduce a graphical version of the the state diagram from the text below,
go to the Graphviz website and download their free tool.
    http://www.graphviz.org/

Mac OSX version:
    http://www.pixelglow.com/graphviz/

$digraph

*/
"""