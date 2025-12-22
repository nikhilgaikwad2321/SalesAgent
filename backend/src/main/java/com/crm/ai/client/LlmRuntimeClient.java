package com.crm.ai.client;

import com.crm.ai.dto.LlmRequestDto;
import com.crm.ai.dto.LlmResponseDto;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.web.client.RestTemplate;

@Component
@RequiredArgsConstructor
public class LlmRuntimeClient {

    private final RestTemplate restTemplate;

    @Value("${llm.runtime.url:http://localhost:8000}")
    private String llmRuntimeUrl;

    public LlmResponseDto generateResponse(LlmRequestDto request) {
        String url = llmRuntimeUrl + "/llm/generate";
        return restTemplate.postForObject(url, request, LlmResponseDto.class);
    }
}
