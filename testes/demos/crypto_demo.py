from cryptography.fernet import Fernet

def demonstrar_criptografia():
    print("--- Demonstração Educacional: Criptografia Simétrica (Fernet) ---")
    
    # 1. Geração de chave
    chave = Fernet.generate_key()
    f = Fernet(chave)
    
    # 2. Mensagem original
    mensagem_original = b"Dados confidenciais da empresa - Projeto Secreto"
    print(f"\nMensagem original: {mensagem_original.decode()}")
    
    # 3. Criptografia (Cifragem)
    token_criptografado = f.encrypt(mensagem_original)
    print(f"Dados criptografados: {token_criptografado}")
    
    # 4. Descriptografia
    mensagem_descriptografada = f.decrypt(token_criptografado)
    print(f"Dados descriptografados: {mensagem_descriptografada.decode()}")

if __name__ == "__main__":
    demonstrar_criptografia()
