from pytest import approx 
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe,pressure_loss_from_fittings
from water_flow import reynolds_number, pressure_loss_from_pipe_reduction

def test_water_column_height(): 
    exp_water_column_height = water_column_height(0.0, 0.0) 
    assert exp_water_column_height == approx( 0.00)

    exp_water_column_height = water_column_height(0.0, 10.0)
    assert exp_water_column_height == approx(7.5)

    exp_water_column_height = water_column_height(25.0, 0.0)
    assert exp_water_column_height == approx(25.0)

    exp_water_column_height = water_column_height(48.3, 12.8)
    assert exp_water_column_height == approx(57.9)

def test_pressure_gain_from_water_height():
    presure_gain = pressure_gain_from_water_height(0.0)
    assert  presure_gain == approx (0.000, abs=0.001)

    presure_gain = pressure_gain_from_water_height(30.2)
    assert presure_gain== approx (295.628, abs=0.001)

    presure_gain = pressure_gain_from_water_height(50.0)
    assert presure_gain == approx (489.450, abs=0.001)

def test_pressure_loss_from_pipe(): 
    pressure_loss = pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75 )
    assert pressure_loss == approx(0.000, abs= 0.001)

    pressure_loss = pressure_loss_from_pipe( 0.048692, 200.00, 0.000 ,1.75)
    assert pressure_loss == approx(0.000, abs= 0.001)

    pressure_loss = pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00)
    assert pressure_loss == approx(0.000, abs= 0.001)

    pressure_loss = pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75)
    assert pressure_loss == approx(-113.008, abs= 0.001)

    pressure_loss = pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65)
    assert pressure_loss == approx(-100.462, abs= 0.001)

    pressure_loss = pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65)
    assert pressure_loss == approx(-61.576, abs= 0.001)

    pressure_loss = pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65)
    assert pressure_loss == approx(-110.884, abs= 0.001)

def test_pressure_loss_from_fittings():
    loss_fiting = pressure_loss_from_fittings(0.00, 3)
    assert loss_fiting == approx(0.000, abs=0.001)

    loss_fiting = pressure_loss_from_fittings(1.65, 0)
    assert loss_fiting == approx(0.000, abs=0.001)

    loss_fiting = pressure_loss_from_fittings(1.65, 2)
    assert loss_fiting == approx(-0.109, abs=0.001)

    loss_fiting = pressure_loss_from_fittings(1.75, 2)
    assert loss_fiting == approx(-0.122, abs=0.001)

    loss_fiting = pressure_loss_from_fittings(1.75, 5)
    assert loss_fiting == approx(-0.306, abs=0.001)

def  test_reynolds_number():
    reynolds_num = reynolds_number(0.048692, 0)
    assert reynolds_num == approx(0, abs= 1)

    reynolds_num = reynolds_number(0.048692, 1.65)
    assert reynolds_num == approx(80069, abs= 1)

    reynolds_num = reynolds_number(0.048692,1.75)
    assert reynolds_num == approx(84922, abs= 1 )

    reynolds_num = reynolds_number(0.286870, 1.65)
    assert reynolds_num == approx(471729, abs= 1)

    reynolds_num = reynolds_number(0.286870, 1.75)
    assert reynolds_num == approx( 500318, abs=	1)

def test_pressure_loss_from_pipe_reduction():
    lost_pipe_reduction= pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692)
    assert lost_pipe_reduction== approx(0.000, abs=0.001)

    lost_pipe_reduction= pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692)
    assert lost_pipe_reduction== approx(-163.744, abs= 0.001)

    lost_pipe_reduction= pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692)
    assert lost_pipe_reduction== approx(-184.182, abs=0.001)



pytest.main(["-v", "--tb=line", "-rN", __file__])

