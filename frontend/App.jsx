import { useState } from 'react'


export default function App() {
const [logs, setLogs] = useState('')
const [question, setQuestion] = useState('')
const [result, setResult] = useState(null)

const analyze = async () => {
   const res = await fetch('http://localhost:8000/analyze', {
     method: 'POST',
     headers: { 'Content-Type': 'application/json' },
     body: JSON.stringify({ logs, question })
    })
    setResult(await res.json())
}


return (
   <div style={{ padding: 20 }}>
      <h2>Offline AI Log Intelligence</h2>
      <textarea rows="8" cols="80" placeholder="Paste logs here" onChange={e => setLogs(e.target.value)} />
      <br />
      <input placeholder="Ask a question" onChange={e => setQuestion(e.target.value)} />
      <br /><br />
      <button onClick={analyze}>Analyze</button>


      {result && (
          <pre>{JSON.stringify(result, null, 2)}</pre>
       )}
     </div>
  )
}
