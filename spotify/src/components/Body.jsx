import React, { useState } from 'react';
import Dropdown from 'react-bootstrap/Dropdown';
import Button from 'react-bootstrap/Button';
//import axios from 'axios';

function Body() {
  const [inputValue, setInputValue] = useState('');
  const [storedHealth, setStoredHealth] = useState('');
  const [storedSleep, setStoredSleep] = useState('');
  const [storedStress, setStoredStress] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log('Input value:', inputValue);
  };

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  const onSelectSleep = (value) => {
    setStoredSleep(value);
  };

  const onSelectHealth = (value) => {
    setStoredHealth(value);
  };

  const onSelectStress = (value) => {
    setStoredStress(value);
  };
  const sendData = async () => {
    const data = {
        ip: inputValue,
        health: storedHealth, 
        sleep: storedSleep,
        stress: storedStress
    };

    await fetch('http://localhost:3000/send_data', {
      method: 'POST',
      headers: {
          "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json()
      .then((data) => {
          console.log('Data sent successfully:', data);
      })
      .catch((error) => {
          console.error('Error sending data:', error);
      }));
  }

  return (
    <>
      <div>
        <form onSubmit={handleSubmit}>
          <label>
            Insert Zipcode
            <input type="text" value={inputValue} onChange={handleChange} />
          </label>
          <button type="Save">Save</button>
        </form>
      </div>
      <br/><br/>
      {storedSleep ? (
        <Dropdown>
          <Dropdown.Toggle variant="success" id="dropdown-basic">
            {`You selected sleep: ${storedSleep}`}
          </Dropdown.Toggle>

          <Dropdown.Menu>
            <Dropdown.Item href="#/action-1" onClick={() => onSelectSleep('1 (poor sleep)')}>
              1 (poor sleep)
            </Dropdown.Item>
            <Dropdown.Item href="#/action-2" onClick={() => onSelectSleep('2 (somewhat poor sleep)')}>
              2 (somewhat poor sleep)
            </Dropdown.Item>
            <Dropdown.Item href="#/action-3" onClick={() => onSelectSleep('3 (generally not good)')}>
              3 (generally not good)
            </Dropdown.Item>
            <Dropdown.Item href="#/action-4" onClick={() => onSelectSleep('4 (very good sleep)')}>
              4 (very good sleep)
            </Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
      ) : (
        <Dropdown>
          <Dropdown.Toggle variant="success" id="dropdown-basic">
            Did you sleep well last night?
          </Dropdown.Toggle>

          <Dropdown.Menu>
            <Dropdown.Item href="#/action-1" onClick={() => onSelectSleep('1 (poor sleep)')}>
              1 (poor sleep)
            </Dropdown.Item>
            <Dropdown.Item href="#/action-2" onClick={() => onSelectSleep('2 (somewhat poor sleep)')}>
              2 (somewhat poor sleep)
            </Dropdown.Item>
            <Dropdown.Item href="#/action-2" onClick={() => onSelectSleep('3 (generally not good)')}>
              3 (generally not good)
            </Dropdown.Item>
            <Dropdown.Item href="#/action-2" onClick={() => onSelectSleep('4 (very good sleep)')}>
              4 (very good sleep)
            </Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
      )}
      <br/><br/>
      {storedHealth ? (
        <Dropdown>
          <Dropdown.Toggle variant="success" id="dropdown-basic">
            {`You selected health: ${storedHealth}`}
          </Dropdown.Toggle>

          <Dropdown.Menu>
            <Dropdown.Item href="#/action-1" onClick={() => onSelectHealth('1 (good)')}>
              1 (good)
            </Dropdown.Item>
            <Dropdown.Item href="#/action-2" onClick={() => onSelectHealth('2 (generally good)')}>
              2 (generally good) 
            </Dropdown.Item>
            <Dropdown.Item href="#/action-3" onClick={() => onSelectHealth('3 (generally not good)')}>
              3 (generally not good)
            </Dropdown.Item>
            <Dropdown.Item href="#/action-4" onClick={() => onSelectHealth('4 (bad)')}>
              4 (bad)
            </Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
      ) : (
        <Dropdown>
          <Dropdown.Toggle variant="success" id="dropdown-basic">
            How good is your health now?
          </Dropdown.Toggle>

          <Dropdown.Menu>
            <Dropdown.Item href="#/action-1" onClick={() => onSelectHealth('1 (good)')}>
              1 (good)
            </Dropdown.Item>
            <Dropdown.Item href="#/action-2" onClick={() => onSelectHealth('2 (generally good)')}>
              2 (generally good) 
            </Dropdown.Item>
            <Dropdown.Item href="#/action-3" onClick={() => onSelectHealth('3 (generally not good)')}>
              3 (generally not good)
            </Dropdown.Item>
            <Dropdown.Item href="#/action-4" onClick={() => onSelectHealth('4 (bad)')}>
              4 (bad)
            </Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
      )}
      <br/><br/>
      {storedStress ? (
        <Dropdown>
          <Dropdown.Toggle variant="success" id="dropdown-basic">
            {`You selected stress: ${storedStress}`}
          </Dropdown.Toggle>

          <Dropdown.Menu>
            <Dropdown.Item href="#/action-1" onClick={() => onSelectStress('1 (a lot)')}>
              1 (a lot)
            </Dropdown.Item>
            <Dropdown.Item href="#/action-2" onClick={() => onSelectStress('2 (a little)')}>
              2 (a little) 
            </Dropdown.Item>
            <Dropdown.Item href="#/action-3" onClick={() => onSelectStress('3 (not much)')}>
              3 (not much)
            </Dropdown.Item>
            <Dropdown.Item href="#/action-4" onClick={() => onSelectStress('4 (none)')}>
              4 (none)
            </Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
      ) : (
        <Dropdown>
          <Dropdown.Toggle variant="success" id="dropdown-basic">
            Do you feel any stress now?
          </Dropdown.Toggle>

          <Dropdown.Menu>
            <Dropdown.Item href="#/action-1" onClick={() => onSelectStress('1 (a lot)')}>
              1 (a lot)
            </Dropdown.Item>
            <Dropdown.Item href="#/action-2" onClick={() => onSelectStress('2 (a little)')}>
              2 (a little) 
            </Dropdown.Item>
            <Dropdown.Item href="#/action-3" onClick={() => onSelectStress('3 (not much)')}>
              3 (not much)
            </Dropdown.Item>
            <Dropdown.Item href="#/action-4" onClick={() => onSelectStress('4 (none)')}>
              4 (none)
            </Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
      )}
      <br/><br/>
      <button type="button" className="btn btn-primary" onClick={sendData}>
        Submit
      </button>
    </>
  );
}

export default Body;
